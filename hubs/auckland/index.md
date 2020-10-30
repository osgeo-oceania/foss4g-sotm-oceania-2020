---
layout: page-with-toc
title: Auckland Hub FOSS4G SotM Oceania 2020
titlecontent: ""
headings: "overview,attend,location,schedule,after-event,speakers,contact-information,sponsors-and-partners"
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

# Location

Our event venue is the HMNZS Philomel Seminar Centre on the grounds of the Devonport Navy Base.
Conference attendees will need to enter the base via the Queens Parade gate.

*As this is a security controlled area we ask that you bring identification in case it is required.*

Ferries depart the city every 15 minutes, and take approximately 10 minutes to reach the Devonport
ferry terminal nearby. From there it is a 10 minute walk from the ferry terminal to the base gate.

<div id="_aklhub_location_map" style="width:100%; height: 400px; border: 1px solid"></div>

<script>
var map = L.map('_aklhub_location_map').setView([-36.8305676,174.7924052], 16);

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
|  2:00 - 4:00 pm | <span style="font-weight: 700">International Streaming Session</span> |
|  4:00 pm | Afternoon Tea<br><small>Tea & coffee supplied</small>          |
|  4:20 pm | Map Showcase & Standups |
|  4:50 - 5:00pm | Closing Remarks        |
|  5:30 pm onwards | After Event Gathering<br><small>See [below](#after-event) for details</small> |

# After Event


Join us from 5:30pm at The Patriot, 14 Victoria Road, Devonport.

Your ticket includes one drink at the bar and finger food.

<div id="_aklhub_afterevent_map" style="width:100%; height: 400px; border: 1px solid"></div>

<script>
var map = L.map('_aklhub_afterevent_map').setView([-36.8299969,174.797735], 16);

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
  margin-bottom: 12px;
}
._akl_speaker_name {
  font-weight: 700;
  font-size: 1.1rem;
}
</style>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Alex Raichev</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Job Accessibility in Auckland, a Data Story</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Dr. Barbara Bollard</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Mapping Antarctica with drones</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Kim Ollivier</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Where is True North</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Callum Mcleod</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Get on your bike - cycle friendly routes using Open Street Maps data</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">James Ford</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Visualizing Bathymetry with Open Source Tools</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Jesse Prendergast</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Access to public open space in Auckland</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Steven Haslemore</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">An enterprise 2d/3d viewer built on open source</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Jordi Tablada</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Mapping iNaturalist records to improve shorebirds conservation efforts in Auckland's west coast</div>
</div>

<div class="_akl_speaker_item">
  <div class="_akl_speaker_name">Hamish Campbell</div>
  <div class="_akl_speaker_org"></div>
  <div class="_akl_speaker_title">Sno: Open Source Data Version Control that Works</div>
</div>


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
