from flask import Flask, render_template, request, redirect, url_for
from python_src.DMA import get_distances
from python_src.TSP import calculate

import os

app = Flask(__name__)

pizzeria_address = None
client_addresses = []
ordered_addresses = []

API_KEY = os.getenv('api_key')

print(API_KEY)

@app.route("/", methods=["GET", "POST"])
def pizzeria():
    global pizzeria_address
    if pizzeria_address:
        return redirect(url_for("clients"))
    if request.method == "POST":
        pizzeria_address = request.form.get("address")
        if pizzeria_address:
            print(f"Pizzeria address: {pizzeria_address}")  
            return redirect(url_for("clients"))  
    return render_template("pizzeria.html", api_key=API_KEY)

@app.route("/clients", methods=["GET", "POST"])
def clients():
    global ordered_addresses
    global client_addresses
    if(len(ordered_addresses) > 0):
        client_addresses = []
        ordered_addresses = []
        return redirect(url_for("clients"))
    print(client_addresses)
    if request.method == "POST":
        client_address = request.form.get("address")
        if client_address:
            client_addresses.append(client_address)
            print(f"Added client address: {client_address}")  
    return render_template("clients.html", pizzeria_address=pizzeria_address, client_addresses=client_addresses, api_key=API_KEY)

@app.route("/calculate_route", methods=["POST"])
def calculate_route():
    global pizzeria_address
    global client_addresses
    global ordered_addresses
    if not pizzeria_address or not client_addresses:
        return redirect(url_for("clients"))

    all_addresses = [pizzeria_address] + client_addresses
    distance_matrix = get_distances(all_addresses, API_KEY)
    print(distance_matrix)
    best_path, total_distance = calculate(distance_matrix)

    ordered_addresses = [all_addresses[i] for i in best_path]
    return render_template("route.html", ordered_addresses=ordered_addresses, total_distance=total_distance)

if __name__ == "__main__":
    app.run()