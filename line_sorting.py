# -*- coding: utf-8 -*-
from collections import defaultdict

lines = '''L#$KJ#()JSEFS(DF)(SD*F
#KJ$H#K$JH@#K$JHD)SF
SDFLKJ#{P@$OJ{SDPFODS{PFO{
#K$HK#JHSFHD(*SHF)SF{HP
#L$H@”#$H”@#L$KH#”@L$K
#~L$KJ#:$SD)FJ)S(DJF)(S
#$KJH#$
SDLKFJD(FJ)SDJFSDLFKS
~L#$KJ:@LK$#J$
LSJDF(S*JDF(*SJDF(*J(DSF*J
'''


positions = defaultdict(list)
list_of_lines = lines.splitlines()

for line in list_of_lines:
	character_pos = 0 
	for character in line:
		positions[character_pos].append(character)
		character_pos += 1


for position,character_list in positions.iteritems():
	print position, len(character_list)
