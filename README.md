# Demo CDK project using GitHub Actions

This project uses AWS CDK to deploy a Lambda function written in Python, with automatic deployment using GitHub Actions.

## Project Structure

```
demo_cdk/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── src/
│   ├── infra/
│   │   └── stacks/
│   │       └── lambda_stack.py
│   │
│   └── services/
│       └── lambda/
│           └── hello_lambda.py
│
├── tests/
│   └── unit/
│       └── test_lambda_stack.py
│
├── app.py
├── cdk.json
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or later
- AWS CLI configured with appropriate credentials
- Node.js and npm (for AWS CDK CLI)
- GitHub account (for GitHub Actions)

## Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd demo_cdk
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Install the AWS CDK CLI:
   ```
   npm install -g aws-cdk
   ```

## GitHub Actions Workflow

This project includes a GitHub Actions workflow for automatic deployment. The workflow is triggered on pushes to the `main` branch and pull requests to the `main` branch. It can also be manually triggered.

### Workflow Steps:

1. Set up Python
2. Install dependencies
3. Configure AWS credentials
4. Deploy the CDK stack

### Setting up GitHub Actions

To use the GitHub Actions workflow:

1. Push your code to a GitHub repository.

2. In your GitHub repository, go to Settings > Secrets and variables > Actions.

3. Add the following secrets:

   - `AWS_ACCESS_KEY_ID`: Your AWS access key ID
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key

4. The workflow will now run automatically on pushes to `main` or can be manually triggered from the Actions tab.

## Manual Deployment

If you prefer to deploy manually, you can use the following steps:

1. Synthesize the CloudFormation template:

   ```
   cdk synth
   ```

2. Deploy the stack:
   ```
   cdk deploy
   ```

## Testing

Run the unit tests with pytest:

```
pytest
```

## Useful CDK Commands

- `cdk ls` List all stacks in the app
- `cdk synth` Emits the synthesized CloudFormation template
- `cdk deploy` Deploy this stack to your default AWS account/region
- `cdk diff` Compare deployed stack with current state
- `cdk docs` Open CDK documentation

## Cleaning Up

To avoid incurring future charges, remember to destroy the resources when you're done:

```
cdk destroy
```

## Contributing

Instructions for how to contribute to the project, if applicable.

## License

MIT.
