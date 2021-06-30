from tkinter import *
from PIL import ImageTk, Image
import requests
import json

weather_color = ""

root = Tk()
root.title("Weather App")
root.geometry("450x100")
root.resizable(False, False)


def zipLookup():

    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + str(zip.get()) + "&distance=5&API_KEY=E017F472-B6B1-4A5C-A6AD-CFE4C6120308")
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        quality = api[0]["AQI"]
        category = api[0]["Category"]["Name"]

        if category == "Good":
            weather_color = "green"
        elif category == "Moderate":
            weather_color = "yellow"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "orange"
        elif category == "Unhealthy":
            weather_color = "red"
        elif category == "Very Unhealthy":
            weather_color = "purple"
        else:
            weather_color = "maroon"

        root.configure(bg=weather_color)
        global myLabel
        myLabel.grid_forget()
        myLabel = Label(root, text=city + " Air Quality " +
                        str(quality) + " " + category, font=("Halvetica", 14), background=weather_color)
        myLabel.grid(row=1, column=0, columnspan=2, pady=10, padx=(10, 0))

    except Exception as e:
        api = "Error..."


zip = Entry(root)
zip.grid(row=0, column=0, padx=20, pady=10, ipadx=10, stick=W+E+S+N)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, padx=20, pady=10, ipadx=5, stick=W+E+S+N)

myLabel = Label(root, text="")

root.mainloop()
