import re

# Main program loop
while True:

    # Project title
    print("=" * 45)
    print("📧 EMAIL EXTRACTOR AUTOMATION TOOL 📧")
    print("=" * 45)

    # Open and read text file
    try:
        with open("sample.txt", "r") as file:
            data = file.read()

    # Handle missing file error
    except FileNotFoundError:
        print("❌ sample.txt file not found!")
        continue

    # Extract all email addresses using regex
    emails = re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        data
    )

    # Remove duplicate emails
    emails = list(set(emails))

    print("\n✅ Extracted Emails:\n")

    # Display total unique email count
    print(f"📊 Total Unique Emails Found: {len(emails)}")

    # Display extracted emails
    for email in emails:
        print(email)

    # Save extracted emails to output file
    with open("extracted_emails.txt", "w") as output_file:

        for email in emails:
            output_file.write(email + "\n")

    print("\n✅ Emails saved to extracted_emails.txt")

    # Ask user to run the program again
    replay = input("\nDo you want to extract emails again? (y/n): ").lower()

    # Exit program
    if replay != "y":
        print("\n👋 Thank you for using Email Extractor Tool!")
        break