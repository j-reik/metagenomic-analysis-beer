import pysam
samfile = pysam.AlignmentFile("Gose1_Weissbier.bam", "rb")

#fetch -> alle Sequencen einlesen
#grep ">" Metagenom.fa gibt alle ID"s aus -> Liste erstellen und durchgehen um Spezies herauszufinden
#Indices aus Metagenom.fa entnehmen und Spezies zuordnen, da auf unertschiedliche ID's gemapped

sequences = []
unmapped = 0
mapped = 0
for r in samfile.fetch(until_eof=True):
    if r.is_unmapped:
        unmapped += 1
    else:
        mapped += 1
    print(r.nsegments)

print(unmapped)
print(mapped)
        


