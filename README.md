# A Process for Monitoring the Impact of Architecture Principles on Sustainability: An Industrial Case Study

This repository is a companion page for the following manuscript:

> Markus Funke, Patricia Lago, Roberto Verdecchia, Roel Donker. 2023. A Process for Monitoring the Impact of Architecture Principles on Sustainability: An Industrial Case Study

It contains further material regarding the submitted manuscript and all material required for reproducing particular research phases and make the study transparent.

Quick Links
---------------

* [Case_Study_Protocol.pdf](misc/case_study_protocol.pdf)

* [Appendix - Results for 'Governance & Security'](results/PRSMT_DM_SQ_Gov-Sec.pdf)
* [Appendix - Results for 'PCS Messaging Portal'](results/PRSMT_DM_SQ_PCS-Messaging.pdf)
* [Appendix - Results for 'PCS Market Portal'](results/PRSMT_DM_SQ_PCS-Market.pdf)
* [Appendix - Results for 'PCS Core'](results/PRSMT_DM_SQ_PCS-Core.pdf)

* [Measurement Tools](results/Measurement_Tools.pdf)
* [Spider Charts](results/Spider_Charts.pdf)


Repository Structure
---------------
This is the root directory of the repository. The directory is structured as follows:

```
/figures
    |---/_sources
            |--- *.drawio.xml
                    Figures raw sources for draw.io
    |--- *.png, *.pdf
            Contains all produced and used figures throughout this research.


/misc
    |--- case_study_protocol.pdf
            Represents the case study protocol and the case study checklist created and used throughout this research.


/Phase_1
    |--- Interview_*
            Interview slides (one per interview group)
    |--- Interview-Protocol_*
            Interview transcripts (one per interview group) => *omitted*


/Phase_2
    |--- Interview#2_*
            Interview slides (one per interview group)
    |--- Interview-Protocol_*
            Interview transcripts (one per interview group) => *omitted*
    |--- KPI_Tools_Overview
            Spreadsheet that contains a list of all considered tools and their KPI mapping as well as the mapping on the sustainability dimensions and QAs
    |--- Mapping_IT-Strategy-Sustainability
            Spreadsheet that contains a preliminary mapping of Schiphol's IT & Data Strategy to the KPIs
    |--- Workingfiles_Principles_PRSM_DecisionMap.drawio.xml
            Draw.io sheet including all FINAL decision maps and PRSM+T models
            All final models are named FINAL
            AND
            all intermediate results (including Phase 1 and Phase 2), like intermediate decision maps


/Phase_3
    |---/spider-charts
        |---/rawData
                |--- KPI_Tools_RawValues.xlsx
                        Spreadsheet that summarises the analysed and used KPI (raw) values.
                |--- PCS_availability.pdf => *omitted*
                |--- PCS_BIA.xls => *omitted*
                |--- PCS_SPLUNK.csv => *omitted*
                |--- PCS_Qualys.csv => *omitted*
        |---/python
                |--- plots_*.py
                        One spider chart per architectural principle
                |--- normalization_mock.py
                        mix-max noramlization based on randomized data (mock data)
                |--- plots_norm.py
                        spider chart for mock data / normalized data
    |---/focus-group
            |--- FocusGroup.pdf
                    Focus group slides
            |--- FocusGroup-Protocol.pdf
                    Focus group transcript

/results
    |--- Key_Performance_Indicators.pdf
            Final set of KPIs
    |--- Measurement_Tools.pdf
            Final set of measurement tools
    |--- PRSMT_DM_SQ_*.pdf
            PRSM+T model; Decision Maps; SQ models for all four architectural tiers
              - Governance & Security
              - PCS Messaging Portal
              - PCS Market Portal
              - PCS Core
    |--- Spider_Charts.pdf
            Spider charts for all four architectural tiers
    |--- Spider_Chart_Normalized.pdf
            Spider chart based on normalized mock data
```
