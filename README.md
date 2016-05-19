# iomb - input-output model builder
iomb is a package for creating environmentally extended input-output models. 

## Data tables
The model is build an top of a set of data tables with a defined format. Some of
these tables are direct input into the model (input tables) and some of them are
generated as intermediate or final results (output tables). All tables are 
stored as Excel files under the `data` folder. The input tables that can be 
modified are located under the `input` sub-directory. The `output` sub-directory
is recreated every time the model is executed.

### Economic model

#### Input tables

##### industries.xlsx
This table contains the identifiers of the industries of the economic model in the
fist column of the 'Industries' sheet. The first row contains is ignored as the
column header. In each other row the first column should contain the identifier
of the respective industry as it is used in the make and use tables.
 
##### commodities.xlsx

 
io_model = iomb.io_matrix(make_table, use_table)
sat_model = iomb.sat_matrix([tables])

iomb.create_olca_pack(io_model, sat_model, sector_infos, flow_infos)