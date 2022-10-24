from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Permission scopes required by the API.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


def main():
    """ Authenticate and authorize with Google Sheets API """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


def create(spreadsheet_id):
    """ Create a new spreadsheet """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Creates new pivot table on the sheet
    try:
        service = build('sheets', 'v4', credentials=creds)
        body = {
            'requests': [{
                'addSheet': {
                    "properties": {
                        "title": "Pivot Table"
                    }
                }
            }]
        }
        spreadsheet = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        source_sheet_id = spreadsheet.get('replies')[0] .get('addSheet').get('properties').get('sheetId')
        print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
        return source_sheet_id
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def get_values(spreadsheet_id, range_name):
    """ Get values based on a range """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        print(f"{len(values)} rows retrieved")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def update_values(spreadsheet_id, range_name, value_input_option, values):
    """ Update values based on a range """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,
                                                        range=range_name, valueInputOption=value_input_option, body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def convert_number(column_int):
    """ Convert a number to an Excel column letter """
    quot, rem = divmod(column_int - 1, 26)
    return convert_number(quot) + chr(rem + ord('A')) if quot else chr(rem + ord('A'))


def value_bool(rows, cols):
    """ Fill the pivot table with boolean values """
    false_value = []
    values = []
    for i in range(0, cols):
        false_value.append('False')
    for j in range(rows - 1):
        values.append(false_value)
    return values


def calculate_country_values(sheet_id, all_data, base_columns, country_list):
    """ Calculate the values of the countries """
    for value in all_data:
        for i in range(1, len(base_columns)):
            if value[0] == base_columns[i][0]:
                for j in range(0, len(country_list)):
                    if value[2] == country_list[j][0]:
                        row = str(i+2)
                        col = convert_number(j + 3)
                        index = col+row
                        update_values(sheet_id, "'Pivot Table'!" + index, "USER_ENTERED", [['True']])


def calculate_themes_values(sheet_id, all_data, base_columns, themes_list, country_list):
    """ Calculate the values of the themes """
    for value in all_data:
        for i in range(1, len(base_columns)):
            if value[0] == base_columns[i][0]:
                for j in range(0, len(themes_list)):
                    if value[3] == themes_list[j][0]:
                        row = str(i+2)
                        col = convert_number(j + 3 + len(country_list))
                        index = col+row
                        update_values(sheet_id, "'Pivot Table'!" + index, "USER_ENTERED", [['True']])


def pivot_table(spreadsheet_id, sheetId, start_row, end_row, start_col, end_col):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)

        body_requests = [{
            "mergeCells": {
                "range": {
                    "sheetId": sheetId,
                    "startRowIndex": start_row,
                    "endRowIndex": end_row,
                    "startColumnIndex": start_col,
                    "endColumnIndex": end_col
                },
                "mergeType": "MERGE_ALL"
            }
        }]

        body = {
            'requests': body_requests
        }
        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        return response

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


if __name__ == '__main__':
    main()

    SPREADSHEETID = '1uUrOMM_n2gtf1TjFNiKj4UC_fC6Z-XN06c_Yfvrwipo'
    # Pass: spreadsheet_id
    PIVOT = create(SPREADSHEETID)

    # Pass: spreadsheet_id and range_name
    all_values = get_values(SPREADSHEETID, "A2:D").get('values', [])
    base = get_values(SPREADSHEETID, "A:B").get('values', [])
    countries = get_values(SPREADSHEETID, "C2:C").get('values', [])
    themes = get_values(SPREADSHEETID, "D2:D").get('values', [])

    # get unique values for countries, themes and authors
    unique_base_columns = []
    for x in base:
        if x not in unique_base_columns:
            unique_base_columns.append(x)

    unique_country_list = []
    country_columns = []
    for x in countries:
        if x not in unique_country_list:
            unique_country_list.append(x)
    country_columns.append(sum(unique_country_list, []))
    country_end_letter = convert_number(len(unique_country_list) + 2)

    unique_themes_list = []
    theme_columns = []
    for x in themes:
        if x not in unique_themes_list:
            unique_themes_list.append(x)
    theme_columns.append(sum(unique_themes_list, []))
    theme_start_letter = convert_number(len(unique_country_list) + 3)
    theme_end_letter = convert_number(len(unique_country_list) + 2 + len(unique_themes_list))

    # fills with false
    false_list = value_bool(len(unique_base_columns), len(
        unique_country_list) + len(unique_themes_list))

    update_values(SPREADSHEETID, "'Pivot Table'!C1", "USER_ENTERED", [['Countries']])
    update_values(SPREADSHEETID, "'Pivot Table'!" + theme_start_letter + "1", "USER_ENTERED", [['Themes']])
    update_values(SPREADSHEETID, "'Pivot Table'!A2:B", "USER_ENTERED", unique_base_columns)
    update_values(SPREADSHEETID, "'Pivot Table'!C2:" + country_end_letter + "2", "USER_ENTERED", country_columns)
    update_values(SPREADSHEETID, "'Pivot Table'!" + theme_start_letter + "2:2", "USER_ENTERED", theme_columns)
    update_values(SPREADSHEETID, "'Pivot Table'!C3:"+theme_end_letter + str(len(unique_base_columns)+1), "USER_ENTERED", false_list)

    pivot_table(SPREADSHEETID, PIVOT, 0, 1, 2, len(unique_country_list)+2)
    pivot_table(SPREADSHEETID, PIVOT, 0, 1, len(unique_country_list) + 2, len(unique_themes_list) + len(unique_country_list)+2)

    # calculate where to put true or false depending on the data
    calculate_country_values(SPREADSHEETID, all_values, unique_base_columns, unique_country_list)
    calculate_themes_values(SPREADSHEETID, all_values, unique_base_columns, unique_themes_list, unique_country_list)
