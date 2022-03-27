
-- test table

CREATE TABLE oac_tw
(
  loc INTEGER, --NOT NULL,
  loc_zn VARCHAR(20),
  loc_name VARCHAR(50),
  loc_purp_desc VARCHAR(2),
  loc_qti VARCHAR(3),
  flow_ind VARCHAR(1),
  DC INTEGER,
  OPC INTEGER,
  TSQ INTEGER,
  OAC INTEGER,
  IT VARCHAR(1),
  auth_over_ind VARCHAR(1),
  nom_cap VARCHAR(1),
  all_qty_avail VARCHAR(1),
  qty_reason VARCHAR(30),
  day DATE,
  cycle VARCHAR(10),
  PRIMARY KEY(loc, loc_purp_desc, day, cycle)
);