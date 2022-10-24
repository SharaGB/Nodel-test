# Nodel Test
![nodel](https://user-images.githubusercontent.com/90220978/197424636-63b5e6e3-eb92-415c-8259-fb0aac10cccd.png)

This repository contains 3 challenges for the Nodel test

### Installation 🔧
Use [git](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to clone this repository in your local machine

```bash
git clone https://github.com/SharaGB/Nodel-test.git
```

### Usage 👾
<code>Challenge 1:</code> Given the [sheet](https://docs.google.com/spreadsheets/d/1uUrOMM_n2gtf1TjFNiKj4UC_fC6Z-XN06c_Yfvrwipo/edit#gid=0), generate a pivot table.

To start, you must execute the following command:
```bash
python 1-pivot_table.py
```
A new tab will open where Google will ask you to log in and verify yourself. Once you log in, a <code>token.json</code> file containing the access tokens will be created.

If you want to change something, add or delete data, you must delete the ***Pivot Table*** that is created in the Google sheet.

<code>Challenge 2:</code> Monty Hall's problem

![WhatsApp Image 2022-10-23 at 7 02 45 PM](https://user-images.githubusercontent.com/90220978/197424872-44def626-5a54-45cf-affa-d8f0793d5243.jpeg)

The simplest solution to the Monty Hall problem is intuitive. The probability of choosing the door with the vehicle as the prize is 1 out of 3 (⅓). Meanwhile, the chance of losing is ⅔.
<br>
That is, if he keeps his initial choice he maintains ⅓ chance of success. On the other hand, if he changes his choice the probability of winning the vehicle increases to ⅔.

Therefore, the Monty Hall problem shows that the participant must change his choice to maximize his probabilities of choosing the car.

Can changing the door influence the outcome of the contest? As we now have two doors to choose from we would think that we have a 50% chance of getting it right, however, this is not the case and it turns out that we have a 66% chance of winning if we change the door we initially chose.
<br>
This can be seen in the following results with 100000 or 1000000 attempts:

```bash
    100,000 games were played
    Chances of winning if you change your choice: 66.58%  
    Chances of winning if you stay with your choice 33.42%

    1,000,000 games were played
    Chances of winning if you change your choice: 66.67%  
    Chances of winning if you stay with your choice 33.33%
_______________________________________________________________________________________________ 
            Now we add a door to the game.

    100,000 games were played
    Chances of winning if you change your choice: 49.86% 
    Chances of winning if you stay with your choice 25.18%
    Chances of winning if Monty Hall open the door with the car 24.96%

    1,000,000 games were played
    Chances of winning if you change your choice: 50.06%
    Chances of winning if you stay with your choice 24.94%
    Chances of winning if Monty Hall open the door with the car 25.00%
```

<code>Challenge 2:</code>: Mouse Exercises with Selenium.

The challenge in this challenge is to use SELENIUM to create a script that will allow you to
script that allows to advance in the different levels of the page interacting with the elements and following the
the elements and following the commands shown.

To see how to automate run:
```bash
python 3-selenium_test.py
```
A new window will open in Chrome and you will be able to see how, without the help of the mouse, each challenge is completed. 🎉

## Authors 🖋️

* [__Shara García__](https://www.linkedin.com/in/sharagb/)
