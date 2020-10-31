#! /usr/local/bin/python3

presentations = {
    "community_presentations": [
        {
            "name": "Damien Hassan",
            "organisation": "State Records Office of Western Australia",
            "presentation_title": "RetroMaps: Adventures in Time and Space"
        },
        {
            "name": "Norm Santich",
            "organisation": "Landgate",
            "presentation_title": "Using open source solutions to deliver spatial applications for government"
        },
        {
            "name": "Dan Dixon",
            "organisation": "University of Western Australia",
            "presentation_title": "Using Satellite and Drone Remote Sensing to monitor Eucalypt Flowering Events"
        },
        {
            "name": "Jenny Smith",
            "organisation": "Landgate",
            "presentation_title": "A non-technical tale of Data WA open source discovery"
        },
        {
            "name": "James Spath",
            "organisation": "City of Swan",
            "presentation_title": "All Take, No Give (LGAs  - Open Data and FOSS4G)"
        },
        {
            "name": "Piers Higgs",
            "organisation": "Gaia Resources",
            "presentation_title": "How Open Source Created a Company"
        },
        {
            "name": "Ross Gillis",
            "organisation": "Hydrobiology",
            "presentation_title": "Open source remote sensing and dashboarding – surface water monitoring at your fingertips"
        },
        {
            "name": "Nimalika Fernando",
            "organisation": "Curtin University",
            "presentation_title": "Let's map indoors: starting indoor mapping with OSM "
        },
        {
            "name": "Emma Krantz",
            "organisation": "CSIRO's Data61",
            "presentation_title": "3D Data Formats: A Field Guide for Geospatial Folks"
        },
        {
            "name": "Gabriel Diosan",
            "organisation": "City of Canning",
            "presentation_title": "A Local Government Journey with QGIS"
        },
        {
            "name": "John Duncan",
            "organisation": "University of Western Australia",
            "presentation_title": "Mapping Tongan farms with QField"
        },
        {
            "name": "Ivana Ivánová",
            "organisation": "Curtin University",
            "presentation_title": "UN peacebuilding & peacekeeping is going….OPEN!"
        },
    ],
    "lightning_talks": [
        {
            "name": "Petra Helmholz",
            "organisation": "Curtin University",
            "presentation_title": "From Applied Cartography students to the QGIS developers with love"
        },
        {
            "name": "Jianhong Cecilia Xia",
            "organisation": "Curtin University",
            "presentation_title": "Time Series Forecasting Of COVID-19 in Australia"
        },
        {
            "name": "Alex Chapman",
            "organisation": "Gaia Resources",
            "presentation_title": "Open and Dynamic Field Guides"
        },
        {
            "name": "James Keating",
            "organisation": "Hydrobiology",
            "presentation_title": "Into the deep – Hydrographic surveying using open source applications"
        },
        {
            "name": "Katherine Allan",
            "organisation": "Landgate",
            "presentation_title": "Discovering WA Government Data"
        },
        {
            "name": "John Bryant",
            "organisation": "Mammoth Geospatial",
            "presentation_title": "OpenStreetMap Data Pacific"
        },
        {
            "name": "Bryan Boruff",
            "organisation": "The University of Western Australia",
            "presentation_title": "The future impact of R-code changes on tree canopy cover: a Nedlands story"
        },
        {
            "name": "Rocio Peyronnet",
            "organisation": "The University of Western Australia",
            "presentation_title": "A multi-sensor machine learning method to map flooding after cyclone events"
        },
        {
            "name": "Khan Mohammed Sazzadur Rahman",
            "organisation": "The University of Western Australia",
            "presentation_title": "Assessing the cooling effect of urban vegetation in Perth"
        },
        {
            "name": "Merindah Bairnsfather-Scott",
            "organisation": "Winyama",
            "presentation_title": "IMW Australia - On Demand"
        },
        {
            "name": "Camilo Vargas",
            "organisation": "Malaria Atlas Project, Telethon Kids Institute",
            "presentation_title": "Using open geospatial data and technology to support malaria risk modelling"
        },
        {
            "name": "Sam Wilson",
            "organisation": "",
            "presentation_title": "Contributing to OpenStreetMap"
        }
    ]
}


template = """
<div class="speaker_bio">
    <h4 id="#name-speaker-id#">#name# - #organisation#</h4>
    <img src="assets/bios/#name-id#.jpg">

    <p><b>Title:</b> #presentation_title#</p>

    <p><b>Abstract:</b> #abstract#</p>

    <p><b>Biography:</b> #biography#</p>
</div>
"""

replacements = ["name", "organisation", "presentation_title", "abstract", "biography"]

# community_presentations or lightning_talks
talk_type = "lightning_talks"

for speaker in presentations[talk_type]:
    talk = template
    for replacement in replacements:
        if replacement in speaker:
            if replacement == "name":
                talk = talk.replace(f"#{replacement}#", speaker[replacement])
                talk = talk.replace("#name-speaker-id#", speaker[replacement].lower().replace(" ", "-") + "-" + talk_type.replace("_", "-")[:-1])
                talk = talk.replace("#name-id#", speaker[replacement].lower().replace(" ", "-"))
            elif replacement == "organisation":
                if speaker[replacement] == "":
                    talk = talk.replace(" - #organisation#", "")
                else:
                    talk = talk.replace(f"#{replacement}#", speaker[replacement])
            else:
                talk = talk.replace(f"#{replacement}#", speaker[replacement])
        else:

            talk = talk.replace(f"#{replacement}#", "TBA")

    print(talk)
