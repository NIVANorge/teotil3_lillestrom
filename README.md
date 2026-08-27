# TEOTIL3 Lillestrøm

Using monitoring and modelling to assess water quality in catchments draining to Lillestrøm kommune.

See the [project website](https://nivanorge.github.io/teotil3_lillestrom/) for details.

## Notebook links

Direct links to code notebooks are given below:

 * [Notebook 01: Catchment maps](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/01_catchment_properties.ipynb)
 * [Notebook 02: Data download](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/02_vannmiljo_vann-nett_nve.ipynb)
 * [Notebook 03a: Annual concentrations for stations](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/03a_annual_concs_stations.ipynb)
 * [Notebook 03b: Annual concentrations for waterbodies](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/03b_annual_concs_waterbodies.ipynb)
 * [Notebook 04a: Annual loads for stations](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/04a_annual_loads_stations.ipynb)
 * [Notebook 04b: Annual loads for waterbodies](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/04b_annual_loads_waterbodies.ipynb)
 * [Notebook 05: Estimates inputs from "spredt" and wastewater overflows](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/05_estimate_overflows_and_spredt.ipynb)
 * [Notebook 06: Build model input files and run TEOTIL3](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/06_build_input_run_model.ipynb)
 * [Notebook 07a: Compare TEOTIL3 to observed data for monitoring stations](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/07a_compare_teotil3_stations.ipynb)
 * [Notebook 07b: Compare TEOTIL3 to observed data for waterbodies](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/07b_compare_teotil3_waterbodies.ipynb)
   

## Project tasks

The main tasks from the project proposal are summarised below.

### Task 1: Download monitoring data

From the proposal:

> Relevante overvåkingsdata for nedbørfeltene vil bli lastet ned fra Vannmiljø og koblet til informasjon om vannkvalitetstilstand hentet fra Vann-Nett. Datasettene vil bli standardisert og kvalitetssjekket (f.eks. for å fjerne ekstreme avvik).
>
> Lillestrøm kommune vil gi veiledning om de beste overvåkingsstasjonene/tidsseriene for sine nedbørfelt. Overvåkingsdata som ikke allerede er tilgjengelige via Vannmiljø kan også leveres av kommunen, om ønskelig (f.eks. ved bruk av en standard Excel-mal).

 * **Notebook 02** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/02_vannmiljo_vann-nett_nve.ipynb)) downloads relevant data from Vannmiljø, Vann-Nett and NVE.
   
 * Monitoring stations suggested by Lillestrøm kommune are in the Excel file [here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/data/lillestrom_monitoring_sites.xlsx).

### Task 2: Monitored nutrient inputs

From the proposal:

> Årlig næringsstofftilførsler i hvert nedbørfelt vil bli estimert ved å kombinere målte kjemiske konsentrasjoner (Oppgave 1) med vannføringsdata fra NVE.
> 
> Der kjemiske målestasjoner er i nærheten av NVE-stasjoner, vil vannføringsdata lastes ned via NVEs HydAPI og skaleres for å matche nedbørfeltet til den kjemiske målestasjonen. Der vannføringsovervåking ikke er tilgjengelig, vil vannføring bli estimert ved hjelp av modellresultater fra NVEs GTS API (med kvalitetskontroll mot observerte data, der det er mulig).
> 
> Årlig næringsstofftilførsler vil bli beregnet fra målte konsentrasjoner og daglig vannføring ved hjelp av den robuste OSPAR-metodikken (samme metoden som brukes for årlig rapportering til OSPAR og innenfor f.eks. Elveovervåkingsprogrammet).

 * **Notebook 02** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/02_vannmiljo_vann-nett_nve.ipynb)) compares NVE's measured data for Sagelva to simulated discharge obtained from the GTS API.

 * **Notebooks 03a and 03b** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/03a_annual_concs_stations.ipynb) and [here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/03b_annual_concs_waterbodies.ipynb)) quality check the Vannmiljø data by removing large outliers, then calculate annual mean concentrations for years with at least 12 samples per year. The Mann-Kendall and Sen's slope tests are used to investigate **trends in concentration**.

 * **Notebooks 04a and 04b** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/04a_annual_loads_stations.ipynb) and [here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/04b_annual_loads_waterbodies.ipynb)) estimate annual loads from the cleaned concentration data using the OSPAR method. The Mann-Kendall and Sen's slope tests are used to investigate **trends in annual loads**.

### Task 3: Customise TEOTIL3 to use local datasets

From the proposal:

> Lillestrøm kommune vil levere data som beskriver (i) regnvann- og nød-overløp fra avløpsnettet, og (ii) utslipp fra private avløpsrenseanlegg. Data vil bli levert for så mange år og parametere som mulig.
> 
> Datasettene vil bli renset og utvidet til å inkludere alle hovedparameterne som er relevante for TEOTIL3 (TOTN, TOTP, TOC og SS). Hull i tidsseriene vil bli fylt ved interpolasjon og, om mulig, ekstrapolert til å dekke perioden fra 2013 til 2023.
> 
> For regine-enheter i Lillestrøm kommune vil det rensede datasettet som beskriver regnvann- og nød-overløp bli brukt til å forbedre de enkle, fast-prosent overløpsestimatene som ble antatt under Oslofjordprosjektet. Tilsvarende vil de detaljerte dataene for private avløpsrenseanlegg erstatte standard TEOTIL3-estimatene for utslipp fra «spredt avløp» (som er basert på aggregerte data).

 * **Notebook 05** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/05_estimate_overflows_and_spredt.ipynb)) estimates nutrient inputs from spredt and wastewater overflows using site-specific data provided by Lillestrøm kommune. New estimates are compared to aggregated data previously provided by SSB.

 * **Notebook 06** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/06_build_input_run_model.ipynb)) builds input files for TEOTIL3 using Lillestrøm kommune's site-specific spredt and overflow data, and then runs the model.

### Task 4: Source-apportioned nutrient inputs from TEOTIL3

From the proposal:

> For nedbørfeltene i Tabell 1 vil årlige næringsstofftilførselen simulert av TEOTIL3 fra 2013 til 2023 bli sammenlignet med estimater basert på overvåkingsdata (Oppgave 2). Modellens ytelse vil bli evaluert, og viktige usikkerheter og begrensninger vil bli diskutert. Der modellens ytelse er tilstrekkelig, vil TEOTIL3 bli brukt til å gi en oversikt over de viktigste næringsstoffkildene i hvert nedbørfelt (naturlig, avløpsrensing, jordbruk osv.).
> 
> I tillegg vil det bli levert et datasett som viser kildefordelte tilførsler til hver regine-enhet i Lillestrøm kommune i henhold til TEOTIL3. Merk at dette datasettet vil være basert på modellinndata (dvs. før transport, akkumulering og retensjon i det hydrologiske nettverket) og inneholder betydelig usikkerhet på regine-skala.
> 
> Viktige punktkilder til næringsstoffer fra avløps- og industri-anlegg i hvert nedbørfelt vil bli identifisert ved hjelp av TEOTIL3-databasen (Figur 1). For avløpsanlegg vil typiske renseeffekter bli beregnet basert på historiske inn- og ut-strømninger rapportert til Miljødirektoratet via ALTINN. Dagens effektivitet vil bli diskutert i sammenheng med nye krav i det oppdaterte avløpsdirektivet og scenariene som er vurdert i det nylig gjennomførte modelleringsprosjektet for Oslofjorden.
> 
> **Merk:** TEOTIL3 er egnet for vurderinger i store nedbørfelt som dekker flere REGINE-enheter. Noen av nedbørfeltene fremhevet av Lillestrøm kommune er enten svært små (f.eks. Jeksla, 17 km2) eller opptar bare én REGINE-enhet (Rømua og Åa) – se Tabell 1. TEOTIL3 forventes ikke å gi gode resultater for disse nedbørfeltene, men modellen vil bli brukt så langt det er rimelig for å evaluere de viktigste næringsstoffkildene.

 * **Notebooks 07a and 07b** ([here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/07a_compare_teotil3_stations.ipynb) and [here](https://github.com/NIVANorge/teotil3_lillestrom/blob/main/code/07b_compare_teotil3_waterbodies.ipynb)) compare measured loads to source-apportioned annual fluxes simulated by TEOTIL3 (see example below for Leira).

### Task 5: Scenarios of reduced nutrient inputs

From the proposal:

> Scenarioene som er utviklet for Oslofjord-modelleringsprosjektet vil bli brukt til å undersøke hvor mye næringsstofftilførselen til nedbørfeltene i Tabell 1 og regine-enheter i Lillestrøm kommune kan endre seg under (i) et scenario med middels ambisjon, og (ii) et scenario med høy ambisjon. Scenariene vurderer oppgraderinger av avløpsrenseanlegg og tiltakspakker for å redusere næringsstofftap fra jordbruk.
> 
> **Merk:** Jordbrukstiltak simulert av NIBIO for Oslofjord-prosjektet er underbygd av grove romlige datasett. Tildelingen av jordbrukstap til spesifikke REGINE-enheter er derfor usikker. Scenarieresultater for større nedbørfelt (Nitelva og Leira) vil sannsynligvis være robust. For nedbørfelt som dekker bare en REGINE-enhet (Rømua og Åa) representerer imidlertid resultatene fra jordbruksmodelleringen gjennomsnittlige forhold i regionen og fanger derfor ikke opp lokale effekter.

 * **In progress.**

### Task 6: Load reductions for Good Ecological Status

From the proposal:

> For nedbørfelt der ytelsen til TEOTIL3 er tilstrekkelig, vil modellen bli brukt til å estimere avlastningsbehovet for God Økologisk Tilstand i henhold til Vanndirektivet. Fordi TEOTIL3 bare simulerer næringsstofftilførsler (nitrogen, fosfor, organisk materiale osv.), vil avlastningsbehovene kun beregnes for de viktigste fysisk-kjemiske vannkvalitetselementene, og ikke for biologiske elementer som bunnfauna, alger osv.
> 
> Merk at TEOTIL3 bare kan brukes til å estimere avlastningsbehov der (i) modellen kan simulere dagens forhold på en tilstrekkelig måte (evaluert i oppgave 4), og (ii) for vannforekomster med et tilstrekkelig stort oppstrøms område (dvs. de vannforekomstene som ligger lengst nedstrøms i hvert nedbørfelt av interesse).

 * **In progress.**