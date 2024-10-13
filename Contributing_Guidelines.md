# Contributing Guidelines

Thank you for your interest in contributing to **Genai Domains DREAMDOMAINS**! We welcome contributions from everyone. To ensure a smooth collaboration, please follow these guidelines when contributing to the project.

## How to Contribute

### 1. Fork the Repository and then Clone

Start by forking the repository to create a personal copy under your GitHub account.

```bash
  git clone https://github.com/Khushalsarode/Gen-Domain-Suggestor
  cd Gen-Domain-Suggestor
```

### 2. Create a Branch

Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
```

### 3. Setup Instructions

Before you begin making changes, ensure you have the necessary environment set up for each component of the project.

#### Server

1. Navigate to the server directory:
    ```bash
    cd server
    ```
2. Install the necessary packages:
    ```bash
    npm install
    ```
3. Start the server:
    ```bash
    node server.js
    ```
4. check out link on browser:
   - The server will run at `https://localhost:5000`.

#### Streamlit

1. Navigate to the Streamlit directory:
    ```bash
    cd streamlit
    ```
2. Set up a virtual environment:
   - Follow the instructions from the [Python venv documentation](https://docs.python.org/3/library/venv.html).
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure your environment:
   - Create a `.env` file and add the necessary API keys.
5. Start the Streamlit application:
    ```bash
    streamlit run app.py
    ```
6. checkout the link on broswer:
- The web app will run at `http://localhost:8501`.

#### React Web App

1. Navigate to the React web app directory:
    ```bash
    cd Gen-Domain-Suggestor
    ```
2. Install the necessary packages:
    ```bash
    npm install
    ```
3. Configure your environment:
   - Create a `.env` file and add your Gemini API keys for the APIs to be used (the file has been added).
4. In the `src/pages/domainstatus.js`, add your API key in the `{placeholder}` section.
5. Start the React application:
    ```bash
    npm start
    ```
6. checkout the link on browser:
   - The web app will run at `https://localhost:3000`.

### 4. Make Your Changes

After setting up the environment, feel free to make changes. Please ensure your code adheres to the existing style and conventions of the project.

### 5. Write Tests

If your changes introduce new features or bug fixes, please add tests to validate your changes.

### 6. Commit Your Changes

Commit your changes with a clear and concise commit message. Use the following format:

```bash
git commit -m "Add feature: Describe what you've done"
```

### 7. Push Your Changes

Push your changes to your forked repository:

```bash
git push origin feature/your-feature-name
```

### 8. Open a Pull Request

Navigate to the original repository to submit your changes. Click on "New Pull Request." Provide a description of your changes, reference any relevant issues, and explain your reasoning.

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](./CODE_OF_CONDUCT.md).

## Issues and Feature Requests

If you encounter a bug or have a feature request, please open an issue in the repository. Provide as much detail as possible, including steps to reproduce the issue or your rationale for the feature request.

## Additional Notes

- **Respect Project Structure**: Please maintain the existing folder structure and file organization.
- **Documentation**: If your changes affect the usage or behavior of the project, please update the documentation accordingly.
- **Review Process**: All contributions will be reviewed, and feedback may be provided. Be open to suggestions and changes to your code.

## Questions?

If you have any questions or need further clarification, feel free to reach out by opening an issue or contacting the maintainer at [khushalsarode.in@gmail.com].

Thank you for contributing to **Genai Domains DreamDomains**!
