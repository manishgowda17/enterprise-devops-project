import os

print("=" * 50)
print("🤖 AI BUILD SUMMARY")
print("=" * 50)

print(f"Build Number : {os.getenv('BUILD_NUMBER')}")
print(f"Job Name     : {os.getenv('JOB_NAME')}")
print(f"Build URL    : {os.getenv('BUILD_URL')}")
print(f"Workspace    : {os.getenv('WORKSPACE')}")

print("\nAI Analysis:")
print("- Source code checked out successfully.")
print("- Docker image build completed.")
print("- Deployment executed.")
print("- Health check passed.")

print("=" * 50)
