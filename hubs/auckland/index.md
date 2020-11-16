---
layout: page-with-toc
title: Auckland Hub FOSS4G SotM Oceania 2020
titlecontent: ""
headings: "overview,attend,location,schedule,early-career-spatial-breakfast,after-event,speakers,map-showcase,conference-shirts-and-merchandise,contact-information,sponsors-and-partners"
---

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>

# Overview

We are excited to present the 2020 FOSS4G SotM Conference Auckland Hub.

With COVID-19 restricting travel, this years FOSS4G-SotM conference is a combined online & physical event. Hubs held around the region will host a mix of shared online content and local presentations. There will be opportunities to meet local OSGeo community attendees and hear from a range of speakers.

This years event will be hosted by NZDF at the Devonport Navy Base, a short walk from the Devonport ferry terminal. Morning tea and lunch will be provided on site.

# Attend

  * [Purchase Tickets](https://ti.to/foss4g-oceania/2020-auckland-hub/)

  * [Code of Conduct](/codeofconduct)

  * [Early Career Spatial Breakfast](#early-career-spatial-breakfast)

# Location

Our event venue is the HMNZS Philomel Seminar Centre on the grounds of the Devonport Navy Base.
Conference attendees will need to enter the base via the Queens Parade gate.

*As this is a security controlled area we ask that you bring identification in case it is required.*

Ferries depart the city every 15 minutes, and take approximately 10 minutes to reach the Devonport
ferry terminal nearby. From there it is a 10 minute walk from the ferry terminal to the base gate.

<div id="_aklhub_location_map" style="width:100%; height: 400px; border: 1px solid"></div>

<script>
var map = L.map('_aklhub_location_map', { scrollWheelZoom: false })
  .setView([-36.8305676,174.7924052], 16);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([-36.8305676,174.7884052]).addTo(map)
    .bindPopup('Conference Location: HMNZS PHILOMEL Seminar Centre<br />Devonport Naval Base')
    .openPopup();

L.marker([-36.8305676,174.7908252]).addTo(map)
    .bindPopup('Entry: Queens Parade Gate');

L.marker([-36.8299969,174.797735]).addTo(map)
    .bindPopup('After Event: The Patriot<br/>14 Victoria Road, Devonport');

L.marker([-36.8329616,174.7958966]).addTo(map)
    .bindPopup('Devonport Ferry Terminal - To City');
</script>


# Schedule


|  8:00 am | Registration & Coffee  |
|  9:00 am | Conference Opening     |
|  9:15 - 10:30 am | <span style="font-weight: 700">First Session</span><br />4 talks from our [Auckland Hub speaker list](#speakers)  |
| 10:30 am | Morning Tea<br><small>Tea & coffee supplied</small> |
| 11:00 - 12:30 am | <span style="font-weight: 700">Second Session</span><br />4 talks from our [Auckland Hub speaker list](#speakers) |
| 12:30 noon | Lunch<br><small>Catered lunch, see your ticket for meal selections</small>      |
|  1:30 - 1:50 pm | <span style="font-weight: 700">Third Session</span><br />1 talk from our [Auckland Hub speaker list](#speakers)   |
|  2:00 - 4:00 pm | <span style="font-weight: 700">[International Streaming Session](/programme/)</span><br><small>6 speakers via Oceania-wide video link</small> |
|  4:00 pm | Afternoon Tea<br><small>Tea & coffee supplied</small>          |
|  4:20 pm | Map Showcase & Standups |
|  4:50 - 5:00pm | Closing Remarks        |
|  5:30 pm onwards | After Event Gathering<br><small>See [below](#after-event) for details</small> |

# Early Career Spatial Breakfast

The Early Career Spatial Breakfast is an opportunity for individuals who are new spatial industry, science & software to meet and network over breakfast, sponsored by OSGeo Oceania.

More details will be provided soon. There are limited spaces available by purchasing the _[Full Ticket + Early Career Spatial Breakfast](https://ti.to/foss4g-oceania/2020-auckland-hub/with/full-price-copy-0fda4ff3-7609-426a-b6e0-d7bc5b1bf0c5)_ ticket type on our [hub ticketing page](https://ti.to/foss4g-oceania/2020-auckland-hub).

The Early Career Spatial Breakfast is made possible by "Good Mojo" funding from OSGeo Oceania.

# After Event


Join us from 5:30pm at The Patriot, 14 Victoria Road, Devonport.

Your ticket includes one drink at the bar and finger food.

<div id="_aklhub_afterevent_map" style="width:100%; height: 400px; border: 1px solid"></div>

<script>
var map = L.map('_aklhub_afterevent_map', { scrollWheelZoom: false })
  .setView([-36.8299969,174.797735], 16);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


L.marker([-36.8305676,174.7884052]).addTo(map)
    .bindPopup('Conference Location: HMNZS PHILOMEL Seminar Centre<br />Devonport Naval Base');

L.marker([-36.8305676,174.7908252]).addTo(map)
    .bindPopup('Entry: Queens Parade Gate');

L.marker([-36.8299969,174.797735]).addTo(map)
    .bindPopup('After Event: The Patriot<br/>14 Victoria Road, Devonport')
    .openPopup();

L.marker([-36.8329616,174.7958966]).addTo(map)
    .bindPopup('Devonport Ferry Terminal - To City');
</script>

# Speakers

The following talks will be held in person at the Auckland Hub.

<style>
._akl_speaker_item {
  margin: 16px 0
}
._akl_speaker_name {
  font-weight: 700;
  border-top: 1px solid #999;
  width: 50%;
  margin-top: 24px;
  color: #333;
}
._akl_speaker_org {
  font-size: 0.95rem;
  color: #333;
}
._akl_speaker_title {
  font-weight: bold;
  margin-top: 6px;
  font-size: 1.2rem;
}
._akl_speaker_abstract  {

}
</style>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Alex Raichev – MRCagney</div>
  <div class="_akl_speaker_org">Alex leads the Data Science Team at <a href="https://www.mrcagney.com/" target='_blank'>MRCagney</a>, who analyse and visualise all kinds of civic data (walking, cycling, public transport, housing, etc.) and create beautiful tools with open source software (!) for data-driven decision making.</div>
  <div class="_akl_speaker_title">Job Accessibility in Auckland, a Data Story</div>
  <div class="_akl_speaker_abstract">
    I'll present an armchair study of job accessibility in Auckland, New Zealand and answer, at least approximately, the following questions for a given mode of travel, e.g. public transport, and a given time bound, e.g. 30 minutes.
    <ol><li>Given a point in Auckland, how many jobs can you reach from that point by that mode and within that time bound?</li>
    <li>What percentage of Aucklanders can reach what percentage of jobs by that mode and within that time bound?</li></ol>
    Along the way, i'll describe my methodology and how i implemented it with the following open source tools: Python, Jupyter, GeoPandas, Open Street Map, and Folium.
    By the end of the presentation, you'll learn enough to replicate the study for your geographical area.
  </div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Dr. Barbara Bollard – AUT</div>
  <div class="_akl_speaker_org">Barbara is a senior lecturer in the School of Applied Sciences at AUT. Her research interests are in GIS applications, ecosystem management and spatial ecology. She has over 20 years experience working in government and NGO's in both Australia and New Zealand.</div>
  <div class="_akl_speaker_title">Mapping Antarctica with drones</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Kim Ollivier – Ollivier &amp; Co</div>

  <div class="_akl_speaker_title">Where is True North</div>
  <div class="_akl_speaker_abstract">
    North on a projection is defined as Grid North because it is not True North. When we want to provide a deviation from Magnetic North which is measures from True North we need a further adjustment. I present two ways of calculating the adjustment using python or PROJ7 module and a small Flask based web service.
  </div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Callum Mcleod – Auckland Transport</div>
  <div class="_akl_speaker_org">Callum Mcleod is the Product Owner for the AT Mobile app and journey planning at Auckland Transport. He enjoys the challenge of designing digital experiences that play a critical role in the daily experience of Aucklanders and wants to increase the use of sustainable transport modes.</div>
  <div class="_akl_speaker_title">Get on your bike - cycle friendly routes using Open Street Maps data</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">James Ford – LINZ</div>
  <div class="_akl_speaker_org">Kia ora, I’m a marine geospatial data analyst at LINZ (Land Information New Zealand). I’ve been in this role for the past three years since graduating from Victoria University of Wellington with a degree in geology. I spend my spare time exploring and photographing the natural world. In my role I’ve had the opportunity to explore and visualize the rich bathymetric data that LINZ holds and test out new and innovative ways of doing so. Integrating in my passion for photography and the natural world, and LINZ’s focus on open source tools, I’ve settled on a workflow for producing images that bring out the beauty and complexity of the seafloor. FOSS4G Oceania has presented me with an opportunity to share my learnings and results with the wider GIS community.</div>
  <div class="_akl_speaker_title">Visualizing Bathymetry with Open Source Tools</div>
  <div class="_akl_speaker_abstract">Discover Oceania beneath the surface of the sea and how to transform bathymetric data into images that bring the seafloor to life with colour, detail, and depth. This talk will start out high level and transition to focus on a [mostly] open source workflow which utilizes: QGIS, python, geopandas, H3 (Uber’s global hexagonal spatial index), virtual rasters, and GNU Image Manipulation Program / Photoshop & Lightroom.</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Jesse Prendergast – MRCagney</div>
  <div class="_akl_speaker_org">Jesse Prendergast is a Transport Planner and Analyst with MRCagney NZ. With a BE in Engineering Science and a Masters of Operations Research, Jesse is keen to understand how we can collect and analyse data to improve lives, through creating spaces and movement appropriate for our lifestyles. Jesse has a particular interest in creating simple, interactive tools to increase public awareness of the trends and issues that exist within our cities and towns.</div>
  <div class="_akl_speaker_title">Access to public open space in Auckland</div>
  <div class="_akl_speaker_abstract">
    During the last few months, Aucklanders have been asked to explore their local area, and have rediscovered their local neighbourhoods and the recreational opportunities close to home. I will present a data story about public open space in Auckland, New Zealand in which I seek to answer the following questions.
    <ol><li>How much public open space do residents of central Auckland have access to, without having to drive?</li>
    <li>How many people do each of Auckland’s public open spaces serve, and how many more could they serve into the future?</li>
    </ol>

    Throughout, I'll describe the process, lessons learned, and use of Python, Jupyter, GeoPandas, Open Street Map, and Folium.
    </div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Steven Haslemore – Woods</div>
  <div class="_akl_speaker_org">Steven has been working in the geo industry the last 16 years, spanning almost the full gamut of geo roles, data, dev, analyst, infra & systems. Always keeping half an eye on the FOSS4G world he recently jumped in and is sharing his path.</div>
  <div class="_akl_speaker_title">An enterprise 2d/3d viewer built on open source and Azure</div>
  <div class="_akl_speaker_abstract">This presentation will run through how to setup your own integrated 2d/3d map viewer using TerriaJS, GeoServer & PostGIS against Microsoft Azure.</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Jordi Tablada – Koordinates</div>
  <div class="_akl_speaker_org">Originally a software engineer with a degree from the Barcelona Schools of Informatics, I also hold a MSc (Environmental Science) from the University of Auckland. During my career I've been fortunate enough to work for several companies and non-profits in different countries such as France, Germany, Vietnam, Indonesia, Spain and New Zealand. I recently re-joined <a href="https://koordinates.com" target="_blank">Koordinates</a> as a Software Engineer after having worked for the Department of Conservation as a marine technical advisor.</div>
  <div class="_akl_speaker_title">Mapping iNaturalist records to improve shorebirds conservation efforts in Auckland's west coast</div>
  <div class="_akl_speaker_abstract">
  The New Zealand Dotterel (Charadrius obscurus) is an endangered shorebird species endemic to New Zealand. Threatened by a range of human-induced factors such as loss of habitat, disturbance and introduced mammalian predators, its North Island subspecies (Charadrius obscurus aquilonius) has responded well to conservation management efforts. This talk shows how I use verified observation data from the citizen science platform iNaturalist and open-source tools to map areas of interest that help boost conservation efforts for the NZ Dotterel at Piha beach, Auckland.
  </div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Hamish Campbell – Koordinates</div>
  <div class="_akl_speaker_org">Hamish is Product Manager at <a href="https://koordinates.com" target="_blank">Koordinates</a>, an OSGeo Oceania chartered member and advocate for open data and open source software.</div>
  <div class="_akl_speaker_title">Sno: Open Source Data Version Control that Works</div>
  <div class="_akl_speaker_abstract">Software developers have used version control to manage code change and collaboration for decades, but the data world is still stuck with awkward check-in systems or multiple copies of data files that are difficult to reconcile.

At Koordinates we've built Sno, a data version control system on top of git. Sno provides schema-aware, per-field, multi-dataset version control, in a system that is both familiar to software developers and powerful to data editors. Best of all, it's open source and available today at https://sno.earth

In this talk we'll demonstrate what Sno can do, and discuss why Sno represents a siesmic shift in how data supply chains will work in the coming years.</div>
</div>

# Map Showcase

<em>Map showcase entries have closed</em>

Have you ever wanted to have your maps professionally printed in large scale? We are very excited to announce our Map Showcase! Submit your map PDF by the end of _Friday 13th November_ (one week before the conference) and we will print and display it at the conference. Many thanks to NZDF for making this possible.

## Important Terms & Conditions

  * Maps can be up to A0 size and in full colour.
  * Maps should be exported to PDF and either:
     - emailed directly to [akl-hub@foss4g-oceania.org](mailto:akl-hub@foss4g-oceania.org) if the size is reasonable,
     - or a Dropbox, GDrive or some other internet accessible link supplied to the above address.
     - please include your name and a brief description of the map.
  * You must [purchase a conference ticket](https://ti.to/foss4g-oceania/2020-auckland-hub/).
  * You must include appropriate attribution for data sources.
  * You must only use data sources you have appropriate rights to use for this purpose.
  * The production of the map should use FOSS (open software and/or open data) to some extent.
  * You grant us permission to print and display your map, and to use it for promotional purposes (strictly within the scope of organising and running the conference and future archival purposes)
  * Come prepared to talk briefly about your map.
  * We have a limited print run capacity. We'll try to get as many printed as possible, but map selections are entirely at the discretion of the organising committee.
  * Yes, you get to take it home after the conference!

# Conference Shirts and Merchandise

Conference shirts will _not_ be available on the day of the conference. If you would like to purchase conference shirts or other merchandise to celebrate FOSS4G-SotM Oceania 2020 you can purchase directly online:

  * [FOSS4G SotM Oceania 2020 Globe T-shirt](https://www.redbubble.com/i/t-shirt/FOSS4G-SotM-Oceania-2020-Globe-by-OSGeo-Oceania/61302747.WFLAH)
  * [FOSS4G SotM Oceania 2020 Logo Hoodie](https://www.redbubble.com/i/hoodie/FOSS4G-SotM-Oceania-2020-Logo-by-OSGeo-Oceania/61302650.O16E3)

More options can be found under the [OSGeo Oceania profile](https://www.redbubble.com/people/OSGeo-Oceania/shop).

# Contact Information

You can contact the organising team any time at [akl-hub@foss4g-oceania.org](mailto:akl-hub@foss4g-oceania.org)

# Sponsors and Partners

Thank you to our sponsors and partners:

<style>
a._akl_sponsor_logo {
  text-decoration: none;
  display: inline-block;
  width: 40%;
  min-width: 200px;
  margin: 30px;
  vertical-align: middle;
}
a._alk_sponsor_logo img {

}
</style>
<a class="_akl_sponsor_logo" href="https://koordinates.com" title="Koordinates" target="_blank">
  <img src="/logos/auckland/koordinates.png" />
</a><a class="_akl_sponsor_logo" href="https://locus.co.nz" target="_blank">
  <img src="/logos/auckland/locus.png" />
</a>
