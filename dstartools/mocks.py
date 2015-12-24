#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MockDRatsSocket:
    test_string = """100 Authentication not required
$GPGGA,002442,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*76
[SOB]"=@=@=@n=@YN0DEC~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 59.54.54.53, port 8801[EOB]"""
    test_string += """[SOB]\xdd=@=@=@n=@YN0DEC~~~CQCQCQx\x9c\xab\xab\x8b\x0e\x0c\x0e\x89U\x08\xceHM\xca\xafLO\xcc\xd3Q\xd0\x08\xf7\xd4T\x08OM,\xc9H-R\xf0\xccK\xcbWPS\x08J,I\xcbIM.\xc9/R\xd0U\xf0K-)\xcf/\xca\xd6Q\xc8\xc8/.\xb1R0\xb5\xd435\x01#c\x1d\x85\x82\xfc\xa2\x12\x05\x0b\x0b\x03C\x00)\xea\x1b\xb1[EOB]"""
    test_string_2 = """100 Authentication not required
[SOB]"=@=@=@5=@FK2TJW~~~CQCQCQ~~[QST] Dansville, New York: 83 F (28 C) (Thu, 18 Jul 2013 00:54:00 GMT)[EOB]$$CRC9089,KA2PQJ>APRATS,DSTAR*:/015413h4128.61N/07429.01W>/A=000750ON D-RATS
$GPGGA,215420,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*76
[SOB]"=@=@=@n=@YAB9FT~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 96.40.241.133, port 9000[EOB][SOB]"=@=@?S=@
                                                              W3FDK~~~CQCQCQ~~ring Request[EOB][SOB]?=@=@4G=@AG5S~~~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@??=@AB9FT-3~CQCQCQ~~x?3??/?P??HMʯLO???=@I??[EOB][rOB]?=@=@ti=@KB9JRC~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@f?=@SQ4BJS~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@nP=@KF5QGD~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@K2TJW~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@??=@VE7HUR~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@65=@ZL2ARN~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@M\=@(K4IFX~~~CQCQCQ~~x?3?(M?W?.?S????+Vp?/?+??Qp?r=@?<	?[EOB][SOB]?=@=@W?=@KC7KPG~~CQCQCQ~~x?3?????KU?p?
OB][SOB]?=@=@??=@N3TSZ-L~CQCQCQ~~x?3?I,(?/PH?KQ?4tt=@-?[EOB][SOB]?=@=@}=@W1CGTr~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@4AB9FT~~~CQCQCQ~~x?3r?
 	.I,???SPJ,I?IM.?/R??HMʯLO???=@:\U[EOB][SOB]?=@=@?N=@KA2PQJ~~CQCQCQ~~x?r?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@WW3A~~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@.=@K2TZY~~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@C3=@!KC2PED~~CQCQCQ~~x?3r?H,??L???M-.,M,??"??5	=@[EOB][SOB]"=@=@=@]?=@K2TJW~~~CQCQCQ~~[QST] K2TJW, Hornell, New York[EOB]$GPGGA,210032,4344.405,N,8743.506,W,1,3,0,0,M,0,M,,*72
[SOB]?=@=@9?=@KF5QGD~~N4VIP~~~x?

pv??I??,.??O?=@)?:[EOB][SOB]"=@=@??=@
                                     KF5QGD~~CQCQCQ~~Ping Request[EOB][SOB]?=@r=@?<@(K?[EOB][SOB]?=@=@?=@K2TJW~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@??=@VE7HUR~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@??=@AB9FT-3~CQCQCQ~~x?3??/?P??HMʯLO???=@I??[EOB][rOB]?=@=@f?=@SQ4BJS~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@4G=@AG5S~~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@WW3A~~~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@??=@N3TSZ-L~CQCQCQ~~x?3?I,(?/PH?KQ?4tt=@-?[EOB][SrB]?=@=@?N=@KA2PQJ~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@4AB9FT~~~CQCQCQ~~x?3r?
 	.I,???SPJ,I?IM.?/R??HMʯLO???=@:\U[EOB][SOB]?=@=@}=@W1CGT~~~CQCQCQ~~x?3r????KU?p?
rB][SOB]?=@=@ti=@KB9JRC~~CQCQCQ~~x?3?????KU?p?CQ~~x?3????.(??KW??/-Np?=@R
 	?=@*??[EOB][SOB]?=@=@C3=@!KC2PED~~CQCQCQ~~x?3r?H,??L???M-.,M,??"??5	=r[EOB][SOB]?=@=@.=@K2TZY~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@65=@ZL2ARN~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@W?=@KC7KPG~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@nP=@KF5QGD~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]"=@=@??=@
                                 KF5QGD~~CQCQCQ~~Ping Request[EOB][SOB]?=@=@==rB][SOB]?=@=@?=@K2TJW~~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@??=@AB9FT-3~CQCQCQ~~x?3??/?P??HMʯLO???=@I??[EOB][SOB]?=@=@??=@N3TSZ-L~CQCQCQ~~x?3?I,(?/PH?KQ?4tt=@-?[EOB][SOB]?=@=@4G=@AG5S~~~~rQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@ti=@KB9JRC~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@??=@VE7HUR~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?N=@KA2PQJ~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@f?=@SQ4BJS~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@.=@K2TZY~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@4AB9FT~~~CQCQCQ~~x?3r?
 	.I,???SPJ,I?IM.?/R??HMʯLO???=@:\U[EOB][SOB]?=@=@65=@ZL2ARN~~CQCQCQ~~x?r?????KU?p?
r	?=@*??[EOB][SOB]?=@=@W?=@KC7KPG~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@M\=@(K4IFX~~~CQCQCQ~~x?3?(M?W?.?S????+Vp?/?+??Qp?r=@?<	?[EOB][SOB]?=@=@}=@W1CGT~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@WW3A~~~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@C3=@!KC2PED~~CQCQCQ~~x?3r?H,??L???M-.,M,??"??5	=@[EOB]$$CRC6A34,K4IFX>APRATS,DSTAR*:/020416h3006.42N\08135.37W-/I'm On Everthing
$GPGGA,220421,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*71
[SOB]?=@=@=@ LAP]?=@5B
                    KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]?=@=@=@	]?=@
                                                                    KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]?=@=@=@	]?=@
                                            KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]"=@=@=@n=@YAB9FT~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 96.40.241.133, port 9000[EOB][SOB]?=@=@=@	]?=@
                                                                    KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]?=@=@=@	]?=@
                                            KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]?=@=@=@	]?=@
                    KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]?=@=@=@	]?=@
                                                                    KC7KPG~~N4VIP~~~x?cI??=@?I[EOB][SOB]?=@=@?b=@0NM5RW~~~CQCQCQ~~x?3
                                                       J?T??N?+ITpK?Q?K-W?M??LvTp?53?(=@?
           m[EOB]$GPGGA,211037,4344.405,N,8743.506,W,1,3,0,0,M,0,M,,*76
[SOB]"=@=@=@?=@NS3K~~~~CQCQCQ~~ Love it so far[EOB][SOB]?=@=@nP=@KF5QGD~~CQCQCr~~x?3?????KU?p?
 	?=@*??[EOB][SOB]"=@=@??=@
                                 NS3K~~~~CQCQCQ~~Ping Request[EOB][SOB]?=@=@??=@N3TSZ-L~CQCQCQ~~x?3?I,(?/PH?KQ?4tt=@-?[EOB][SOB]?=@=@M\=@(K4IFX~~~CQCQCQ~~x?r=@?<W?.?[EOB][SOB]?=@=@f?=@SQ4BJS~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@4G=@AG5S~~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@}=@W1CGT~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@??=@VE7HUR~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@WW3A~~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@=}=@NM5RW~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@ti=@KB9JRC~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@W?=@KC7KPG~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@65=@ZL2ARN~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@.=@K2TZY~~~CQCQCQ~~x?3?????KU?p?
r	?=@*??[EOB][SOB]?=@=@nP=@KF5QGD~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]?=@=@??=@AB9FT-3~CQCQCQ~~x?3??/?P??HMʯLO???=@I??[EOB][SOB]?=@=@C3=@!KC2PED~~CQCQCQ~~x?3r?H,??L???M-.,M,??"??5	=@[EOB][SOB]?=@=@?=@4Ar9FT~~~CQCQCQ~~x?3r?
 	.I,???SPJ,I?IM.?/R??HMʯLO???=@:\U[EOB][SOB]?=@=@?N=@KA2PQJ~~CQCQCQ~~x?r?????KU?p?
r	?=@*??[EOB][SOB]?=@=@?=@K2TJW~~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB][SOB]"=@=@=@??=@NNS3K~~~~CQCQCQ~~I've been reading the manual and trying to set up memory channels and the like[EOB][SOB]?=@=@9?=@KF5QGD~~N4VIP~~~x?

pv??I??,.??O?=@)?:[EOB]$GPGGA,221424,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*75
[SOB]"=@=@=@n=@YAB9FT~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 96.40.241.133, port 9000[EOB]$GPGGA,221731,3428.233,N,8425.452,W,1,3,0,490,M,0,M,,*73
$GPGGA,212046,4344.405,N,8743.506,W,1,3,0,0,M,0,M,,*73
[SOB]"=@=@=@??=@=ZNM5RW~~~CQCQCQ~~n5vip,. are you out there?[EOB][SOB]?=@=@?^=rMI3YXX~~CQCQCQ~~x?3?????KU?p?
 	?=@*??[EOB]$$CRCD65A,K4IFX>APRATS,DSTAR*:/022418h3006.42N\08135.37W-/I'm On Everthing
$GPGGA,222426,4003.726,N,7505.448,W,1,3,0,0,M,0,M,,*74
[SOB]"=@=@=@??=@FK2TJW~~~CQCQCQ~~[QST] Dansville, New York: 80 F (27 C) (Thu, 18 Jul 2013 01:54:00 GMT)[EOB][SOB]"=@=@=@??=@MI3YXX~~CQCQCQ~~ hi larry online[EOB][SOB]"=@=@=@n=@YAB9FT~~~CQCQCQ~~[QST] Sheboygan, (WI) Weather Info & Ratflector - Network, host: 96.40.241.133, port 9000[EOB][SOB]"=@=@=@]?=@K2TJW~~~CQCQCQ~~[QST] K2TJW, Hornell, New York[EOB][SOB]"=@=@=@?2=@EMI3YXX~~CQCQCQ~~AB9FT HI LARRY FROM N IRELAND TESTING D-RATS ONLY NEW TO THIS PROGRAM[EOB][SOB]"=@=@=@ҧ=@AB9FT-3~CQCQCQ~~mi3yxx: it's working[EOB][SOB]"=@=@=@x?=@SAB9FT-3~CQCQCQ~~name is Josh, qth: Sheboygan, WI (roughly 50 mi N of Milwaukee along Lake Michigan)[EOB]$GPGGA,213054,4344.405,N,8743.506,W,1,3,0,0,M,0,M,,*71


"""
    index = -1
    def recv(self, byte):
        self.index += 1
        if self.index >= len(self.test_string):
            return
        return self.test_string[self.index]

    def connect(self, (host, port)):
        pass
