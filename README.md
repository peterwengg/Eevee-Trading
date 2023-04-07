![](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)![](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)<img src="https://forthebadge.com/images/badges/uses-git.svg" style="zoom: 67%;" />


# IS213 - G4T4 EEVEE

<div align="center"  style="background-color:white;>
  <a href="https://github.com/Janeleq/G4T4-Eevee">
    <img src="https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png" width="300" height="280" title="Eevee logo" id="is213">
  </a>

<h3 align="center">EEVEE Trading</h3>

  <p align="center">
    EEVEE is a project to make a enteprise solution based on the microservices architecture for a Cryptocurrency scenario using appropriate technologies and tools. 
    <br />
    <a href="https://github.com/Janeleq/G4T4-Eevee"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Janeleq/G4T4-Eevee">View Demo</a>
    ·
    <a href="https://github.com/Janeleq/G4T4-Eevee/issues">Report Bug</a>
    ·
    <a href="https://github.com/Janeleq/G4T4-Eevee/pulls">Request Feature</a>
  </p>


</div>

## Member Information

| Members               | School Email     | Email                           | LinkedIn                                                     |
| --------------------- | ---------------- | ------------------------------- | ------------------------------------------------------------ |
| Jane Lim Enqi         | janelim.2021     | janelim2001@gmail.com           | [@LinkedIn](https://sg.linkedin.com/in/limenqi01)            |
| Sim Jia Cheng Malcolm | malcolm.sim.2021 | malcolmsim7@hotmail.com         | [@LinkedIn](https://sg.linkedin.com/in/malcolm-sim-protocrux) |
| Tan Jia Jin | jiajin.tan.2021  | jjtan.com.jj@gmail.com | [@LinkedIn](https://www.linkedin.com/in/tan-jia-jin/) |
| Tan Quan Wah          | quanwah.tan.2021 | qwtan98@gmail.com               | [@LinkedIn](https://sg.linkedin.com/in/qwtan98)              |
| Weng Jia Yang Peter | jyweng.2021  | weng.jiayang.peter@gmail.com | [@LinkedIn](https://www.linkedin.com/in/peter-wengjiayang/) |



<!-- TABLE OF CONTENTS -->

[TOC]



<!-- ABOUT THE PROJECT -->

## Project Overview

[Go To Top](#is213)

### About the Project
EEVEE Trading, allows for buy/sell requests of currency through market order, buy/sell requests through limit order and swapping of one currency to another. Users are also able to top up their wallet balance to carry out their transactions. Notably, our cryptocurrency platform is meant for simulation purposes and is made in an attempt to closely depict how real trading would be.In the following, we will be covering 4 contextual user scenarios that are relevant in the aforementioned business scenario.

### Project Structure

```
📦G4T4-Eevee
 ┣ 📂 Frontend
 ┃ ┣ 📂 static
 ┃ ┃ ┣ 📂 css
 ┃ ┃ ┣ 📂 images
 ┃ ┃ ┣ 📂 js
 ┃ ┃ ┃ ┣ 📂 coins
 ┃ ┃ ┃ ┣ 📂 homepageWithLogin
 ┃ ┃ ┃ ┣ 📂 Login+Register Page
 ┃ ┃ ┃ ┣ 📜 register.mjs
 ┃ ┃ ┃ ┣ 📜 script-no-ajax.mjs
 ┃ ┃
 ┃ ┣ 📂 template 
 ┃ ┃ ┣ 📂 coins
 ┃ ┃ ┣ 📂 homepageWithLogin
 ┃ ┃ ┣ 📂 images
 ┃ ┃ ┣ 📂 Login+Register Page
 ┃ ┃ ┃ ┣ 📜 Login.html
 ┃ ┃ ┣ 📜 buy_error.html
 ┃ ┃ ┣ 📜 index.html
 ┃ ┃ ┣ 📜 register.html
 ┃ ┃ ┣ 📜 starterpage.html
 ┃ ┃
 ┣ 📂 Backend
 ┃ ┣ 📜 app.py
 ┃ ┣ 📜 check_order.py
 ┃ ┣ 📜 make_transaction.py
 ┃ ┃ 
 ┣ 📂 Kubernetes
 ┃ ┣ 📜 deployment.yml
 ┃ ┣ 📜 service.yml
 ┃ ┃
 ┣ 📜 .dockerignore
 ┣ 📜 app.Dockerfile
 ┣ # gitignore
 ┣ 📜 .gitignore
 ┃
 ┗ 📜 README.md
```



## Technologies Used

[Go To Top](#is213)

### Front End Development (Core Libraries)

> Front End was developed on Node with VUE-CLI.

| Library   | Description                           | Link                                   |
| --------- | ------------------------------------- | -------------------------------------- |
| Flask     | Web Framework                             | [Flask](https://flask.palletsprojects.com/en/2.2.x/) |
| Bootstrap | Tooltips, Toasts, Offcanvas, Carousel | [Bootstrap](https://getbootstrap.com/) |

### Front End Styling

> Bootstrap was the Main Library for styling

| Library / Tool | Description          | Link                                     |
| -------------- | -------------------- | ---------------------------------------- |
| Bootstrap CSS  | Grid, Flex Utilities | [Bootstrap](https://getbootstrap.com/)   |
| AOS            | Animations           | [AOS](https://michalsnik.github.io/aos/) |
| Plotly         | Graphs               | [Plotly](https://plotly.com)             |

### Back End (Core Libraries)

> Back End is coded in Javascript with NodeJS.

| Library | Description                                                | Link                             |
| ------- | ---------------------------------------------------------- | -------------------------------- |
| Flask  | Flask is a micro web framework written in Python. | [Flask](https://flask.palletsprojects.com/en/2.2.x/) |
| NodeJS  | Open-source, cross-platform JavaScript runtime environment | [NodeJS](https://nodejs.org/en/) |
| Docker  | Set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. | [Docker](https://www.docker.com) |

### Version Control

> Project files are hosted on Github 

| Service | Description                                         | Link                         |
| ------- | --------------------------------------------------- | ---------------------------- |
| Github  | Version Control collaborative environment using Git | [Github](https://github.com) |

### External API, Libraries and Extras

| Library / Tool       | Description                                          | Link                                                         |
| -------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| Stripe Payment API    | Provide stock articles news and information          | [Alpha Vantage API](https://www.alphavantage.co/documentation) |
| Google Firebase      | Real-time Database and Authentication                | [Google Firebase](https://firebase.google.com)               |
| CryptoCompare API               | README Editing and Formatting                        | [Typora](https://typora.io)                                  |
| Bootstrap Studio     | Drag and Drop designing of pages                     | [Bootstrap Studio](https://bootstrapstudio.io)               |
| Typora               | README Editing and Formatting                        | [Typora](https://typora.io)                                  |

### External API Gateways

### External Messaging Brokers

[Go To Top](#is213)

### Project Setup [For Developers]

##### Tools Required

| Tool   | Download                                           |
| ------ | -------------------------------------------------- |
| Python3 | [Download Python3](https://www.python.org/downloads/) |

1. Run Docker
2. Run MAMP / WAMP
3. Open 1 terminal (cd backend and run docker-compose up) 
4. Visit the webpage by opening a browser (preferably Google Chrome) and enter http://localhost:5000

pip install -r requirements.txt
```

##### Login Credentials

| Email         | Password |
| ------------- | -------- |
| ape@gmail.com | apeape   |


##### Card Usage
[Utilise Stripe Test Cards](https://stripe.com/docs/testing)


[Go To Top](#is213)
