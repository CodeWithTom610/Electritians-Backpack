<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">ELECTRITIANS-BACKPACK</h1></p>
<p align="center">
	<img src="https://img.shields.io/github/license/CodeWithTom610/Electritians-Backpack?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/CodeWithTom610/Electritians-Backpack?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/CodeWithTom610/Electritians-Backpack?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/CodeWithTom610/Electritians-Backpack?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [🔰 Contributing](#-contributing)


--

## 👾 Features

- Tools for ETIEs/EBTs directly out of your Pocket
- Knowledgebase with file upload for plans etc.
- Admin Panel/Dashboard with user invitation via e-mail.

---

## 📁 Project Structure

```sh
└── Electritians-Backpack/
    ├── LICENSE
    ├── __pycache__
    │   └── config.cpython-312.pyc
    ├── app
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-312.pyc
    │   │   ├── forms.cpython-312.pyc
    │   │   ├── models.cpython-312.pyc
    │   │   ├── routes.cpython-312.pyc
    │   │   ├── tools.cpython-312.pyc
    │   │   └── utils.cpython-312.pyc
    │   ├── forms.py
    │   ├── models.py
    │   ├── routes.py
    │   ├── templates
    │   │   ├── admin-dashboard.html
    │   │   ├── admin_login.html
    │   │   ├── alle_tools.html
    │   │   ├── base.html
    │   │   ├── edit_know_entry.html
    │   │   ├── edit_news.html
    │   │   ├── index.html
    │   │   ├── knowledgebase.html
    │   │   ├── knowledgebase_entry_view.html
    │   │   ├── manage-users.html
    │   │   ├── new-entry-news.html
    │   │   ├── new-user.html
    │   │   ├── new_knowledgebase_entry.html
    │   │   ├── news-management.html
    │   │   ├── reset-password.html
    │   │   ├── widerstandsrechner.html
    │   │   └── wiederstands_tools.html
    │   ├── tools.py
    │   └── utils.py
    ├── config.py
    ├── instance
    │   └── database.db
    ├── migrations
    │   ├── README
    │   ├── __pycache__
    │   │   └── env.cpython-312.pyc
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       ├── 009990be25e2_.py
    │       ├── 0b5006e6eb3a_.py
    │       ├── 1b1e647b7c7e_.py
    │       ├── 27a1081c2876_.py
    │       ├── 2a041ba2ea8c_.py
    │       ├── 42058aa89671_.py
    │       ├── 46aab575cd31_.py
    │       ├── 4a5d6564fabb_.py
    │       ├── 4f6b0567c156_.py
    │       ├── 55ff291eb664_.py
    │       ├── 63f23e3119b3_.py
    │       ├── 6b36d4d40935_.py
    │       ├── 6fd27f6245da_.py
    │       ├── 8b57cb8ed198_.py
    │       ├── 998901780d0c_.py
    │       ├── 9f22b0c469f2_.py
    │       ├── __pycache__
    │       │   ├── 009990be25e2_.cpython-312.pyc
    │       │   ├── 0b5006e6eb3a_.cpython-312.pyc
    │       │   ├── 1b1e647b7c7e_.cpython-312.pyc
    │       │   ├── 27a1081c2876_.cpython-312.pyc
    │       │   ├── 2a041ba2ea8c_.cpython-312.pyc
    │       │   ├── 42058aa89671_.cpython-312.pyc
    │       │   ├── 46aab575cd31_.cpython-312.pyc
    │       │   ├── 4a5d6564fabb_.cpython-312.pyc
    │       │   ├── 4f6b0567c156_.cpython-312.pyc
    │       │   ├── 55ff291eb664_.cpython-312.pyc
    │       │   ├── 63f23e3119b3_.cpython-312.pyc
    │       │   ├── 6b36d4d40935_.cpython-312.pyc
    │       │   ├── 6fd27f6245da_.cpython-312.pyc
    │       │   ├── 8b57cb8ed198_.cpython-312.pyc
    │       │   ├── 998901780d0c_.cpython-312.pyc
    │       │   ├── 9f22b0c469f2_.cpython-312.pyc
    │       │   ├── b33e1a658211_.cpython-312.pyc
    │       │   ├── b392130c381a_.cpython-312.pyc
    │       │   ├── b456849bff17_.cpython-312.pyc
    │       │   ├── c0959040a022_.cpython-312.pyc
    │       │   ├── c51ed0f00dee_.cpython-312.pyc
    │       │   ├── cb90e61780f0_.cpython-312.pyc
    │       │   ├── daa46e763214_.cpython-312.pyc
    │       │   ├── e4143391fb58_.cpython-312.pyc
    │       │   ├── e744cc22f4df_.cpython-312.pyc
    │       │   ├── ee79d1325b80_.cpython-312.pyc
    │       │   ├── f696400303bd_.cpython-312.pyc
    │       │   └── f9e30f2359e0_.cpython-312.pyc
    │       ├── b33e1a658211_.py
    │       ├── b392130c381a_.py
    │       ├── b456849bff17_.py
    │       ├── c0959040a022_.py
    │       ├── c51ed0f00dee_.py
    │       ├── cb90e61780f0_.py
    │       ├── daa46e763214_.py
    │       ├── e4143391fb58_.py
    │       ├── e744cc22f4df_.py
    │       ├── ee79d1325b80_.py
    │       ├── f696400303bd_.py
    │       └── f9e30f2359e0_.py
    ├── requirements.txt
    └── run.py
```
---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Electritians-Backpack, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install Electritians-Backpack using one of the following methods:

**Build from source:**

1. Clone the Electritians-Backpack repository:
```sh
❯ git clone https://github.com/CodeWithTom610/Electritians-Backpack
```

2. Navigate to the project directory:
```sh
❯ cd Electritians-Backpack
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run Electritians-Backpack using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ gunicorn app:create_app()
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/CodeWithTom610/Electritians-Backpack/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/CodeWithTom610/Electritians-Backpack/issues)**: Submit bugs found or log feature requests for the `Electritians-Backpack` project.
- **💡 [Submit Pull Requests](https://github.com/CodeWithTom610/Electritians-Backpack/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/CodeWithTom610/Electritians-Backpack
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/CodeWithTom610/Electritians-Backpack/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=CodeWithTom610/Electritians-Backpack">
   </a>
</p>
</details>

---
