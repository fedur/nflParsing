_TEAM_ACRONYMS = {
	"cowboys": "DAL",
	"patriots": "NE",
	"cardinals": "ARI",
	"falcons": "ATL",
	"ravens": "BAL",
	"bills": "BUF",
	"panthers": "CAR",
	"bears": "CHI",
	"eagles": "PHI",
	"bengals": "CIN",
	"browns": "CLE",
	"broncos": "DEN",
	"packers": "GB",
	"texans": "HOU",
	"colts": "IND",
	"jaguars": "JAX",
	"chiefs": "KC",
	"rams": "LAR",
	"raiders": "OAK",
	"chargers": "LAC",
	"dolphins": "NMIA",
	"vikings": "MIN",
	"saints": "NO",
	"lions": "DET",
	"giants": "NYG",
	"jets": "NYJ",
	"steelers": "PIT",
	"seahawks": "SEA",
	"buccaneers": "TB",
	"49ers": "SF",
	"titans": "TEN",
	"redskins": "WAS"
}

def getAcronym(teamName):
	tName=teamName.strip().lower()
	for key in _TEAM_ACRONYMS.keys():
		if key in tName:
			return _TEAM_ACRONYMS[key]


