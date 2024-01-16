![Funderfest Events logo](assets/funderfest_events_banner_dark_2.png)
# FunderFest Events Back End
Back end repo for She Codes crowdfunding project. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white) ![Insomnia](https://img.shields.io/badge/Insomnia-black?style=for-the-badge&logo=insomnia&logoColor=5849BE) ![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

[![MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

---
FIXME:
[About](#about) ✦ [API Spec](#api_spec) ✦ [DB Schema](#db_schema) ✦ [Resources](#resources) ✦ [License](#license) ✦ [Contact](#contact)

---
## About
### What is FunderFest
This project aim was to create a crowdfunding website. I decided to work with my events and festival background and create a platform for event creators. Funderfest Events allows event creators to sell tickets to their event with the oportunity to get donetions for the event as well. 

### Intended Audience/User Stories

### Front End Pages/Functionality

## API Spec
| URL                                    | HTTP Method | Purpose                                                  | Request Body | Success Response Code | Authentication/Authorisation              |
|----------------------------------------|-------------|----------------------------------------------------------|--------------|-----------------------|-------------------------------------------|
| /festivals/                            | GET         | List all festivals                                       |              | 200                   | None required                             |
| /festivals/                            | POST        | Festival object (without id or date created)             |              | 200                   | Log in required                           |
| /festivals/?is_open=True               | GET         | Return all festivals currently live                      |              | 200                   | None required                             |
| /festivals/?order_by=date_created      | GET         | Return festivals in order of date created                |              | 200                   | None required                             |
| /festivals/?order_by=number_of_pledges | GET         | Return festivals in order of number of pledges           |              | 200                   | None required                             |
| /festivals/?limit=x                    | GET         | Return the number of festivals by the value of x         |              | 200                   | None required                             |
| /festivals/?order_by=recent_pledges    | GET         | Return festivals in order of most recent pledges         |              | 200                   | None required                             |
| /festivals/1                           | GET         | Festivals with pledges field with list of pledge objects |              | 200                   | None required                             |
| /festivals/1                           | PUT         | Festival object (without id)                             |              | 200                   | Log in required and must be project owner |
| /pledges/                              | GET         | Return all pledges made                                  |              | 200                   | None required                             |
| /pledges/?order_by=date_created        | GET         | Return pledges in order of date created                  |              | 200                   | None required                             |
| /pledges/                              | POST        | Pledge object (without id or date created)               |              | 200                   | Log in required                           |
| /api-token-auth/                       | POST        | User object                                              |              | 200                   |                                           |
## DB Schema
![Database schema for funderfest events](assets/funderfest_db_schema.png)
---
## Resources
https://www.tablesgenerator.com

## License

This project is using the following license:

**MIT**

For further information regarding the license, please follow the link below:
https://opensource.org/licenses/MIT

---

## Contact

If you have any further questions, please contact via email or github.

<a href="mailto:caoimhejyoti@gmail.com"><img alt="Link to email contact address" src="https://img.shields.io/badge/email-D14836?style=for-the-badge" target="_blank" /></a> <a href="https://github.com/caoimhejyoti"><img alt="badge for GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" target="_blank" /></a>
