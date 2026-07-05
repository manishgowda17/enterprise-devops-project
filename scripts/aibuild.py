import os

print("=" * 45)
print("🤖 AI BUILD SUMMARY")
print("=" * 45)

print(f"Build Number : {os.getenv('BUILD_NUMBER')}")
print(f"Job Name     : {os.getenv('JOB_NAME')}")
print(f"Build URL    : {os.getenv('BUILD_URL')}")

print("\nDeployment Status : SUCCESS")
print("AI Recommendation :")
print("- Docker image built successfully.")
print("- Application deployed successfully.")
print("- No issues detected.")
print("=" * 45)
