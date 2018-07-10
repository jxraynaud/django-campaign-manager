# django-campaign-manager
Tool to manage advertising campaigns

## Disclaimer
This tool is in alpha version.
There's no guarantee that the tool will be developped or supported in the future.

## Tool Description
This tool is a django app allowing to manage media campaigns from an advertiser perspective, using an adserver and purcharsing on various media platforms.
The objectives are to:
* Get a single database with all the informations (dimensions) on all the ads and placements used.
* Provide high level objects for easy management.
* Automation of some tasks, like transforming a budget allocation into a trafficking template.

## Status

At this stage in the development the objective is to build a consistent ORM. 
To allow fast import/export/modification, we will use two methods to imports files in the database:
* django-import-export module when it doesn't require too many modification of the data and/or include references to higher level objects.
* R scripts to directly process the data and import it into the database using SQL requests.

We are well aware of the fact that it isn't a good idea to get a ORM and use direct SQL requests to import/export data. However it allows faster testing. On the long run we will modify the architecture to use Python scripts, Django forms, and, if nneeded, an api to do this.
