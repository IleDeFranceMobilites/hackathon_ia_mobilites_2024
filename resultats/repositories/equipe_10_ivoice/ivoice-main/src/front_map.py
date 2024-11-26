import folium

def create_map(messages_dict):
 
    paris = [48.8566, 2.3522]
    
    carto = folium.Map(location=paris, zoom_start=12)
    
    stations = [
        "Pont de Sèvres", "Billancourt", "Marcel Sembat", "Porte de Saint-Cloud", "Exelmans", "Michel-Ange - Molitor",
        "Jasmin", "Ranelagh", "La Muette", "Rue de la Pompe", "Trocadéro", "Iéna", "Alma-Marceau", "Franklin D. Roosevelt",
        "Saint-Philippe-du-Roule", "Miromesnil", "Saint-Augustin", "Havre - Caumartin", "Chaussée d'Antin - La Fayette",
        "Richelieu - Drouot", "Grands Boulevards", "Bonne Nouvelle", "Strasbourg - Saint-Denis", "République", "Oberkampf",
        "Saint-Ambroise", "Voltaire", "Charonne", "Rue des Boulets", "Nation", "Buzenval", "Maraîchers", "Porte de Montreuil",
        "Robespierre", "Croix de Chavaux", "Mairie de Montreuil"
    ]

    
    
    latitudes = [
        48.823964, 48.835907, 48.836888, 48.839375, 48.841398, 48.844135, 48.848396, 48.856180, 48.860417, 48.865891,
        48.863516, 48.865298, 48.863292, 48.869229, 48.872070, 48.876091, 48.874364, 48.874632, 48.874384, 48.871696,
        48.870002, 48.869400, 48.867317, 48.866147, 48.863762, 48.861379, 48.857391, 48.852542, 48.847788, 48.849933,
        48.850933, 48.850716, 48.853238, 48.861215, 48.871215
    ]
    
    longitudes = [
        2.233380, 2.239462, 2.246494, 2.259622, 2.264682, 2.268228, 2.273601, 2.278307, 2.280910, 2.282769, 2.288353,
        2.293115, 2.300285, 2.307716, 2.312528, 2.316154, 2.320072, 2.328104, 2.333535, 2.339269, 2.348722, 2.354295,
        2.363048, 2.369687, 2.377587, 2.383494, 2.389027, 2.392810, 2.397401, 2.406544, 2.412216, 2.418861, 2.432307,
        2.440926, 2.446745
    ]
    
        
    
    for station, lat, lon in zip(stations, latitudes, longitudes):
        message_voyageur = messages_dict.get(station)
    
    
        popup_content = f"""<div style="font-size:16px;"><b style="color:blue; font-size:20px;">{station}</b><br><span style="font-size:18px;">{message_voyageur}</span></div>"""
    
    
        folium.Marker([lat, lon], popup=folium.Popup(popup_content, max_width=400, min_width=200)).add_to(carto)
    
    
    html_string = carto.get_root().render()
    return html_string

    #carto.save("stations_map.html")