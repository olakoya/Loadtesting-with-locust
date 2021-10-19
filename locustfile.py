from locust import HttpUser, task, between

class mysiteTesting(HttpUser):

    def on_start(self):
        self.client.get("/maven-tutorials/how-to-execute-selenium-webdriver-testng-xml-using-maven")

    @task(2)
    def index(self):
        print("The index page has loaded")
        self.client.get("/")
    
    
    # @task(1)
    # def analyzer(self):
    #     print("The analyzer page has loaded")
    #     self.client.get("/test")
    
    @task(3)
    def submit_data(self):
        print("The sort, search demo")
        self.client.get("/test/table-sort-search-demo.html")