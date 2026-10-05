import csv,json,pathlib
p=pathlib.Path(__file__).parent
codes='LAX HKG BKK CNX HAN CKG SZB KUL PQC SGN NRT KIX ICN KHH SFO JFK AKL SYD SAN HNL'.split()
a={}
for r in csv.DictReader(open(p/'assets/airports.csv')):
 c=r['iata_code']
 if c in codes and r['type'] in ('large_airport','medium_airport'):
  lat,lon=map(float,r['coordinates'].split(','));a[c]={'lon':lon,'lat':lat,'name':r['name'],'city':r['municipality'],'region':r['iso_country']}
assert len(a)==20,(len(a),set(codes)-set(a))
rows=[
('2025-12-27','LAX','HKG','CX883','Cathay Pacific'),('2025-12-29','HKG','BKK','CX705','Cathay Pacific'),
('2026-01-06','CNX','BKK','','Unspecified'),('2026-01-07','BKK','HKG','CX706','Cathay Pacific'),
('2026-02-05','HKG','HAN','UO540','HK Express'),('2026-02-08','HAN','HKG','UO543','HK Express'),('2026-02-24','HKG','CKG','HX496','Hong Kong Airlines'),
('2026-03-01','CKG','HKG','CA565','Air China'),('2026-03-06','HKG','SZB','UO716','HK Express'),('2026-03-09','KUL','PQC','AK545','AirAsia'),('2026-03-11','PQC','SGN','VN6104','Vietnam Airlines / Pacific'),('2026-03-15','SGN','HKG','VJ876','VietJet Air'),('2026-03-20','HKG','NRT','UO870','HK Express'),('2026-03-24','NRT','KIX','GK215','Jetstar Japan'),('2026-03-29','KIX','NRT','GK230','Jetstar Japan'),('2026-03-30','NRT','HKG','GK27','Jetstar Japan'),
('2026-04-15','HKG','ICN','UO630','HK Express'),('2026-04-19','ICN','HKG','UO627','HK Express'),('2026-05-04','HKG','KHH','UO136','HK Express'),('2026-05-07','KHH','HKG','UO133','HK Express'),('2026-05-09','HKG','SFO','UA862','United'),('2026-05-23','SFO','LAX','AA6428','American / SkyWest'),('2026-05-23','LAX','JFK','AA274','American'),
('2026-07-04','JFK','LAX','AA3','American'),('2026-07-04','LAX','AKL','','Unspecified'),('2026-07-06','AKL','SYD','','Unspecified'),('2026-07-12','SYD','AKL','NZ104','Air New Zealand'),('2026-07-12','AKL','LAX','','Unspecified'),('2026-07-12','LAX','JFK','AA28','American'),('2026-08-14','JFK','SAN','AS35','Alaska'),('2026-08-14','SAN','HNL','AS894','Alaska / Hawaiian'),('2026-08-20','HNL','SFO','UA1646','United')]
f=[]
for i,(d,o,t,n,c) in enumerate(rows):
 user=i in [2,24,25,26,27]
 f.append(dict(id=i,date=d,origin=o,dest=t,number=n,airline=c,evidence='You confirmed' if user else 'Email record',note='Auckland inferred from your New Zealand connection and travel emails; exact flight number unverified.' if i in [24,27] else 'July 6 local date inferred from Sydney arrival evidence; trip began July 4.' if i==25 else 'NZ104 arrival on July 12 supported by your NZ traveller declaration.' if i==26 else 'Airline and Bangkok airport not verified; BKK used for the distance estimate.' if i==2 else ''))
(p/'data.js').write_text('const AIRPORTS='+json.dumps(a)+';\nconst FLIGHTS='+json.dumps(f)+';\nconst WORLD='+ (p/'assets/world.json').read_text()+';')
t=(p/'template.html').read_text()
for marker,file in [('D3','assets/d3.min.js'),('TOPO','assets/topojson.min.js'),('DATA','data.js'),('APP','app.js')]:t=t.replace('/*'+marker+'*/',(p/file).read_text())
(p/'2026-flight-journal.html').write_text(t)
(p/'index.html').write_text(t)
print('Built',p/'2026-flight-journal.html',len(t),'bytes; flights',len(f))
