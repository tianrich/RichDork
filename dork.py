def main():
    print("Google Dork Generator")
    print("=====================")

    while True:
        print("\nOptions:")
        print("1. Search for exact word or phrase")
        print("2. Exclude a word")
        print("3. Search in a specific site")
        print("4. Search for a specific file type")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            query = input("Enter the exact word or phrase: ")
            print(f'"{query}"')
        elif choice == '2':
            query = input("Enter the word you want to exclude: ")
            print(f'-{query}')
        elif choice == '3':
            site = input("Enter the specific site (e.g., example.com): ")
            query = input("Enter the search query: ")
            print(f'site:{site} {query}')
        elif choice == '4':
            file_type = input("Enter the file type (e.g., pdf): ")
            query = input("Enter the search query: ")
            print(f'filetype:{file_type} {query}')
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
