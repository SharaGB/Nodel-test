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
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
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


def countries_values(sheet_id, data, base, countries):
    """ Calculate the values of the countries """
    for value in data:
        for i in range(1, len(base)):
            if value[0] == base[i][0]:
                for j in range(0, len(countries)):
                    if value[2] == countries[j][0]:
                        row = str(i+2)
                        col = convert_number(j + 3)
                        index = col+row
                        update_values(sheet_id, "'Pivot Table'!" + index, "USER_ENTERED", [['True']])


def themes_values(sheet_id, data, base, themes, countries):
    """ Calculate the values of the themes """
    for value in data:
        for i in range(1, len(base)):
            if value[0] == base[i][0]:
                for j in range(0, len(themes)):
                    if value[3] == themes[j][0]:
                        row = str(i+2)
                        col = convert_number(j + 3 + len(countries))
                        index = col + row
                        update_values(sheet_id, "'Pivot Table'!" + index, "USER_ENTERED", [['True']])


def pivot_table(spreadsheet_id, sheetId, startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        service = build('sheets', 'v4', credentials=creds)

        body_requests = {
            'requests': [
                {
                    "mergeCells": {
                        "range": {
                            "sheetId": sheetId,
                            "startRowIndex": startRowIndex,
                            "endRowIndex": endRowIndex,
                            "startColumnIndex": startColumnIndex,
                            "endColumnIndex": endColumnIndex
                        },
                        "mergeType": "MERGE_ALL"
                    }
                }
            ]
        }

        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body_requests).execute()
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

    base_values = []
    for x in base:
        if x not in base_values:
            base_values.append(x)

    country_values = []
    country_columns = []
    for x in countries:
        if x not in country_values:
            country_values.append(x)
    country_columns.append(sum(country_values, []))
    country_end_letter = convert_number(len(country_values) + 2)

    theme_values = []
    theme_columns = []
    for x in themes:
        if x not in theme_values:
            theme_values.append(x)
    theme_columns.append(sum(theme_values, []))
    theme_start_letter = convert_number(len(country_values) + 3)
    theme_end_letter = convert_number(len(country_values) + 2 + len(theme_values))
    boolean = value_bool(len(base_values), len(country_values) + len(theme_values))

    update_values(SPREADSHEETID, "'Pivot Table'!A2:B", "USER_ENTERED", base_values)
    update_values(SPREADSHEETID, "'Pivot Table'!C1", "USER_ENTERED", [['Country']])
    update_values(SPREADSHEETID, "'Pivot Table'!C2:" + country_end_letter + "2", "USER_ENTERED", country_columns)
    update_values(SPREADSHEETID, "'Pivot Table'!" + theme_start_letter + "1", "USER_ENTERED", [['Theme']])
    update_values(SPREADSHEETID, "'Pivot Table'!" + theme_start_letter + "2:2", "USER_ENTERED", theme_columns)
    update_values(SPREADSHEETID, "'Pivot Table'!C3:"+theme_end_letter + str(len(base_values)+1), "USER_ENTERED", boolean)

    pivot_table(SPREADSHEETID, PIVOT, 0, 1, 2, len(country_values)+2)
    pivot_table(SPREADSHEETID, PIVOT, 0, 1, len(country_values) + 2, len(theme_values) + len(country_values)+2)

    countries_values(SPREADSHEETID, all_values, base_values, country_values)
    themes_values(SPREADSHEETID, all_values, base_values, theme_values, country_values)
