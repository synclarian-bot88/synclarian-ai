# Main Application File for Synclarian AI
# This is where everything comes together!

from web_scraper import WebScraper
from local_learner import LocalLearner
from code_generator import CodeGenerator
from config import LOCAL_DATA_PATH
import os

class Synclarian:
    """
    Synclarian - An AI that learns online and offline, then generates code
    """
    
    def __init__(self):
        print("\n" + "="*60)
        print("🤖 Welcome to Synclarian AI!")
        print("="*60)
        
        self.scraper = WebScraper()
        self.learner = LocalLearner()
        self.generator = CodeGenerator()
        self.learning_data = ""
    
    def learn_from_web(self, api_urls):
        """
        Learn from web APIs
        
        Args:
            api_urls (list): List of API URLs to learn from
        """
        print("\n📡 LEARNING FROM WEB APIs...")
        print("-" * 60)
        
        for url in api_urls:
            if url.strip():  # Only process non-empty URLs
                self.scraper.fetch_from_api(url)
        
        # Save what we learned
        self.scraper.save_learned_data()
    
    def learn_from_local_files(self, directory=None):
        """
        Learn from local files and datasets
        
        Args:
            directory (str): Directory path to learn from
        """
        print("\n📂 LEARNING FROM LOCAL FILES...")
        print("-" * 60)
        
        if directory is None:
            directory = LOCAL_DATA_PATH
        
        self.learner.scan_directory(directory)
        self.learner.save_learning_summary()
    
    def generate_code(self, request):
        """
        Generate code based on learning
        
        Args:
            request (str): What code to generate
            
        Returns:
            str: The generated code
        """
        print("\n🔧 GENERATING CODE...")
        print("-" * 60)
        
        # Prepare context from learned data
        context = f"""
        Learned API Data: {len(self.scraper.learned_data)} sources
        Learned Local Files: {len(self.learner.learned_files)} files
        """
        
        self.generator.set_learned_context(context)
        
        # Generate the code
        code = self.generator.generate_code(request)
        return code
    
    def save_code(self, code, filename):
        """
        Save generated code (NEVER DELETES)
        
        Args:
            code (str): The code to save
            filename (str): Filename to save as
        """
        return self.generator.save_generated_code(code, filename)
    
    def show_menu(self):
        """
        Show the interactive menu for Synclarian
        """
        print("\n" + "="*60)
        print("SYNCLARIAN AI - MAIN MENU")
        print("="*60)
        print("1. Learn from Web APIs")
        print("2. Learn from Local Files")
        print("3. Generate Code")
        print("4. View Learning Summary")
        print("5. Exit")
        print("="*60)
    
    def run(self):
        """
        Run Synclarian in interactive mode
        """
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                print("\nEnter API URLs (comma-separated):")
                print("Example: https://jsonplaceholder.typicode.com/posts/1")
                urls_input = input("URLs: ")
                urls = [url.strip() for url in urls_input.split(',')]
                self.learn_from_web(urls)
            
            elif choice == '2':
                print("\nEnter directory path (or press Enter for default):")
                directory = input("Path: ").strip()
                if not directory:
                    directory = LOCAL_DATA_PATH
                self.learn_from_local_files(directory)
            
            elif choice == '3':
                request = input("\nWhat code do you want to generate?\nRequest: ")
                code = self.generate_code(request)
                
                if code:
                    print("\n" + "="*60)
                    print("GENERATED CODE:")
                    print("="*60)
                    print(code)
                    print("="*60)
                    
                    save_choice = input("\nSave this code? (yes/no): ").strip().lower()
                    if save_choice == 'yes':
                        filename = input("Filename (e.g., my_code.py): ").strip()
                        if filename:
                            self.save_code(code, filename)
            
            elif choice == '4':
                print("\n" + "="*60)
                print("LEARNING SUMMARY")
                print("="*60)
                print(f"API Sources Learned: {len(self.scraper.learned_data)}")
                print(f"Local Files Learned: {len(self.learner.learned_files)}")
                print(f"Code Generated: {len(self.generator.generated_codes)}")
                print("="*60)
            
            elif choice == '5':
                print("\n👋 Thank you for using Synclarian AI!")
                print("="*60 + "\n")
                break
            
            else:
                print("\n⚠ Invalid choice. Please try again.")

# Example quick usage (no interactive menu)
def quick_demo():
    """
    Quick demo showing how to use Synclarian programmatically
    """
    print("\n" + "="*60)
    print("🤖 SYNCLARIAN AI - QUICK DEMO")
    print("="*60 + "\n")
    
    synclarian = Synclarian()
    
    # Step 1: Learn from a public API
    print("Step 1: Learning from Web API...")
    synclarian.learn_from_web([
        "https://jsonplaceholder.typicode.com/posts/1"
    ])
    
    # Step 2: Learn from local files
    print("\nStep 2: Learning from local files...")
    synclarian.learn_from_local_files(LOCAL_DATA_PATH)
    
    # Step 3: Generate code
    print("\nStep 3: Generating code...")
    code = synclarian.generate_code("Create a Python function that fetches data from an API and returns it as JSON")
    
    if code:
        print("\n" + "="*60)
        print("GENERATED CODE:")
        print("="*60)
        print(code)
        print("="*60 + "\n")
        
        # Step 4: Save the code
        synclarian.save_code(code, "api_fetcher.py")

# Run the application
if __name__ == "__main__":
    print("\nChoose mode:")
    print("1. Interactive Menu")
    print("2. Quick Demo")
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        synclarian = Synclarian()
        synclarian.run()
    else:
        quick_demo()
