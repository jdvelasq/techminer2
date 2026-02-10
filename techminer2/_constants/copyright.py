COPYRIGHT = frozenset(
    sorted(
        r"""
, applied solar energy , \d{4} ,
, berlin boston \.
, berlin/boston \.
, chinese academy of agricultural sciences \.
, inc \.
, inc \.$
, proceedings \. all rights reserved \.$
, wiesbaden \d{4} \. alle rechte vorbehalten \.
. \d{4} asme$
. csp cambridge , uk \. i and s florida , usa , \d{4}$
(\b[a-z]+\b\s)*asociacion(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*conference proceeding(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*conference proceedings(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*conference(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*conferencia(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*elsevier(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*gmbh(,*\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*inderscience(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*institute(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*instituto(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*journal(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*revista(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*special issue(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*springer naature b \. v
(\b[a-z]+\b\s)*springer(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*springer(\s\b[a-z\+]+\b)* \. v
(\b[a-z]+\b\s)*taylor and francis(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*universidad(\s\b[a-z\+]+\b)* , (\b[a-z]+\b\s) \.$
(\b[a-z]+\b\s)*universitas(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)*universitat(\s\b[a-z\+]+\b)* , (\b[a-z]+\b\s) \.$
(\b[a-z]+\b\s)*university(\s\b[a-z\+]+\b)* , (\b[a-z]+\b\s) \.$
(\b[a-z]+\b\s)*verlag(\s\b[a-z\+]+\b)*
(\b[a-z]+\b\s)+press
/ licenses / by/ 4\.0/ \) \.$
/ licenses / by/4\.0/ \) .$
\. ((\b[a-z]+\b\s)*, )*(\b[a-z]+\b\s)+\d{4} \.$
\. (\b[a-z]+\b\s)+, \d{4} \.$
\. (\b[a-z]+\b\s)+publications , \d{4} \.
\. (\b[a-z]+\b\s)+society$
\. \( \d{4} \) , \( brno university of technology \) \.
\. \( \d{4} \) , \( elite scientific publications \) \.
\. \( \d{4} \) , \( insight society \) \.
\. \( \d{4} \) , \( iscap information systems and computing academic professionals \) \.
\. \( \d{4} \) , \( kluwer law international \) \.
\. \( \d{4} \) , \( neutrosophic sets and systems \) \.
\. \( \d{4} \) , \( science and information organization \) .
\. \( \d{4} \) , \( social sciences research society \) \.
\. \( \d{4} \) , \( uikten association for information communication technology education and science \) \.
\. \( \d{4} \) , \( universiti putra malaysia \) \.
\. \( \d{4} \) by association for information systems \( ais \) all rights reserved \.
\. \( \d{4} \) by ecos \d{4} all rights reserved \.$
\. \( 2024 \) , \( halmstad university \) \. all rights reserved \.
\. \{4} , korean finance association \.
\. \d{3} , no copyright protection is available for such works under us law \.
\. \d{4 babita singla , kumar shalender and nripendra singh \.$
\. \d{4} , ((\b[a-z]+\b\s)*, )*((\b[a-z]+\b\s)*and )(\b[a-z]+\b\s)*\.$
\. \d{4} , ((\b[a-z]+\b\s)*, )*\.$
\. \d{4} , (\b[a-z]+\b\s)*ltd .
\. \d{4} , (\b[a-z]+\b\s)+\.$
\. \d{4} , (\b[a-z]+\b\s)+society \.
\. \d{4} , \d{4} american statistical association \.
\. \d{4} , \d{4} economic research forum \.
\. \d{4} , academic conferences and publishing international limited \.
\. \d{4} , academy of management \.
\. \d{4} , academy of sciences of the czech republic , institute of state and law \.
\. \d{4} , advances in engineering education \.
\. \d{4} , agricultural economics \.
\. \d{4} , aidic servizi s \. are \. l \.
\. \d{4} , algerian centre for the development of renewable energy \.
\. \d{4} , allied business academies \.
\. \d{4} , american public health association inc \.
\. \d{4} , american scientific publishing group \( aspg \) \.
\. \d{4} , annals of family medicine , inc \.
\. \d{4} , anpad associacao nacional de pos graduacao e pesquisa them administracao \.
\. \d{4} , asers publishing house \.
\. \d{4} , associacao brasileira de engenharia de producao \.
\. \d{4} , associacao iberica de sistemas e tecnologias de informacao \.
\. \d{4} , association for industry , engineering , and management systems \( aiems \) \.
\. \d{4} , association for information systems \.
\. \d{4} , bentham books imprint \.
\. \d{4} , boom uitgevers .
\. \d{4} , boom uitgevers \.
\. \d{4} , bulgarska akademiya na naukite \.
\. \d{4} , canadian center of science and education \.
\. \d{4} , centro universitario curitiba unicuritiba \.
\. \d{4} , cognitione foundation for the dissemination of knowledge and science \.
\. \d{4} , collegium basilea \.
\. \d{4} , consiglio nazionale delle ricerche \.
\. \d{4} , curran associates inc \.
\. \d{4} , dei tipografia del genio civile \.
\. \d{4} , der\/die autor : in \.$
\. \d{4} , dr d \. pylarinos \.
\. \d{4} , ebru bagci \.
\. \d{4} , econjournals \.
\. \d{4} , economic and social studies \.
\. \d{4} , economic laboratory for transition research \.
\. \d{4} , editoriale scientifica srl \.
\. \d{4} , eesti pollumajandusulikool \.
\. \d{4} , european association for the development of renewable energy , environment and power quality \( ea4epq \) \.
\. \d{4} , fabio creta and francesca tenca \.
\. \d{4} , facultad de informatica , universidad nacional de la plata \.
\. \d{4} , global energy interconnection development and cooperation organization \.
\. \d{4} , high voltage engineering editorial department of cepri \.
\. \d{4} , innovative information science and technology research group \.
\. \d{4} , insitute of geography and spatial organization polish academy of sciences \.
\. \d{4} , institute of renewable energy national academy of sciences of ukraine \.
\. \d{4} , institution of structural engineers \.
\. \d{4} , international association for energy economics \.
\. \d{4} , international association of engineers \.
\. \d{4} , international group for lean construction \.
\. \d{4} , international organization on ' technical and physical problems of engineering ' \.
\. \d{4} , iquz galaxy publisher \.
\. \d{4} , ismail saritas \.
\. \d{4} , istanbul teknik universitesi , faculty of architecture \.
\. \d{4} , istituto zooprofilattico dell'abruzzo e del molise \.
\. \d{4} , japan section of the regional science association international \.
\. \d{4} , journal of economic issues / association for evolutionary economics \.$
\. \d{4} , journalof industrial engineering and engineering management \.
\. \d{4} , korean finance association \.
\. \d{4} , korean marketing association \.
\. \d{4} , lembaga contrarius indonesia \.
\. \d{4} , lexxion verlagsgesellschaft mbh \.
\. \d{4} , libyan center for solar energy research and studies \.
\. \d{4} , malaysian consumer and family economics association \.
\. \d{4} , marketing management association \.
\. \d{4} , mdpi ag \.
\. \d{4} , middle pomeranian scientific society of the environment protection \.
\. \d{4} , national environmental health association \.
\. \d{4} , national research university , higher school of econoimics \.
\. \d{4} , oga osterreichische gesellschaft fur agrarokonomie \.
\. \d{4} , pan american health organization \.
\. \d{4} , paulus editora \.
\. \d{4} , penerbit akademia baru \.
\. \d{4} , penerbit universiti kebangsaan malaysia \.
\. \d{4} , penerbit uthm \.
\. \d{4} , periodicals of engineering and natural sciences \.
\. \d{4} , politeknik negeri padang \.
\. \d{4} , public administration school of catalonia \.
\. \d{4} , research and innovation centre pro akademia \.
\. \d{4} , research trend \.
\. \d{4} , research trends \.
\. \d{4} , russian academy of sciences \.
\. \d{4} , russian presidental academy of national economy and public administration \.
\. \d{4} , scanditale ab \.
\. \d{4} , science press \( china \) \.
\. \d{4} , societa italiana degli economisti \( italian economic association \) \.
\. \d{4} , solar energy periodical office co \.
\. \d{4} , srac romanian society for quality \.
\. \d{4} , srac societatea romana pentru asigurarea calitatii \.
\. \d{4} , strojarski facultet \.
\. \d{4} , thomas a \. lyson center for civic agriculture and food systems \.
\. \d{4} , universidad andina simon olivar , sede ecuador \.
\. \d{4} , universiti teknologi mara \.
\. \d{4} , university of cienfuegos , carlos rafael rodriguez \.
\. \d{4} , university of zagreb , faculty of organization and informatics \.
\. \d{4} , uts epress \.
\. \d{4} , verlag barbara budrich \.
\. \d{4} , with intelligence \.
\. \d{4} , world academy of research in science and engineering \.
\. \d{4} , world association for sustainable development \.
\. \d{4} , world health organization \.
\. \d{4} , wydawnictwo uniwersytetu marii curie sklodowskiej w lublinie \.
\. \d{4} , zbw leibniz information center for economics \.
\. \d{4} . nsp natural sciences publishing cor \.
\. \d{4} ((\b[a-z]+\b\s)*, )*published by de gruyter \.
\. \d{4} (\b[a-z]+\b\s)*consortium(\s\b[a-z\+]+\b)* \.
\. \d{4} (\b[a-z\+]+\b\s)+\.$
\. \d{4} \. asers publishing \.
\. \d{4} \. cbiore ijred \.
\. \d{4} \. journal of content , community and communication \.
\. \d{4} \. polissia national university \.
\. \d{4} \. rigeo \.
\. \d{4} \. the authors license this article under the terms of the creative commons attribution \d\.0 license \.
\. \d{4} \. universiti tun hussein onn malaysia publisher ' s office \. all rights reserved \.$
\. \d{4} \( tojia cinque \) \.
\. \d{4} a. carbone editore \.
\. \d{4} academy of management \.
\. \d{4} academy of medical sciences of i\.r \. iran \.
\. \d{4} aee world energy engineering congress \.
\. \d{4} african journal of science , technology , innovation and development \.$
\. \d{4} ais icis administrative office \.
\. \d{4} amer \. soc \. heating , ref \. air conditoning eng \. inc \.
\. \d{4} american public health association inc \.
\. \d{4} american statistical association \.
\. \d{4} annual reviews inc \.
\. \d{4} anpad associacao nacional de pos graduacao e pesquisa them administracao \.
\. \d{4} antai college of economics and management , shanghai jiao tong university \.
\. \d{4} apple academic press , inc \.
\. \d{4} article authors$
\. \d{4} ascociacion internacional de economia aplicada \.
\. \d{4} asean university network / southeast asia engineering education development network \.
\. \d{4} asean university network\/southeast asia engineering education development network \.
\. \d{4} asociacion cuadernos de economia . todos los derechos reservados \.$
\. \d{4} association for computing machinery \.
\. \d{4} association pour le traitement automatique des langues \.
\. \d{4} aubrey milunsky and jeff m \. milunsky \.
\. \d{4} author \( s \) \.
\. \d{4} author \( s \) \( or their employer \( s \) \.
\. \d{4} author \( s \)$
\. \d{4} babita singla , kumar shalender and nripendra singh \.
\. \d{4} barbu liliana , published by sciendo \.
\. \d{4} bayramukov s\.h\. , dolaeva z \. n \.
\. \d{4} beijing xintong media co \.
\. \d{4} bharati vidyapeeth , new delhi \.
\. \d{4} biblioteca nacional de cuba jose marti \.
\. \d{4} boeck universite \.
\. \d{4} bremer , plaisance , walker , bonn , love , perrone and sarker \.$
\. \d{4} brian towers \( britow \) and john wiley and sons ltd \.
\. \d{4} bright publisher \.
\. \d{4} business informatics \.
\. \d{4} by author / s and licensed by modestum \.
\. \d{4} by author\/s and licensed by modestum \.$
\. \d{4} by dr \. umesh r \. hodeghatta and umesha nayak \.
\. \d{4} by georgetown university , pew case study center , usa \.
\. \d{4} by gert h \. n \. laursen \.
\. \d{4} by koninklijke brill nv , leiden , the netherlands \.$
\. \d{4} by nova science publishers , inc \.
\. \d{4} by the authors . licensee : region \.
\. \d{4} by the authors \. licensee esj , italy \.
\. \d{4} by the haworth press , inc \.
\. \d{4} by the you \. s \. chamber of commerce , except for chapter \d{1,2} , which is a work of the you \. s \.
\. \d{4} by thomas w \. dinsmore \.
\. \d{4} canadian association of geographers / l ' association canadienne des geographes \.
\. \d{4} canadian association of geographers l ' association canadienne des geographes \.
\. \d{4} certified financial planner board of standards , inc \.
\. \d{4} ceur ws \.
\. \d{4} china international book trading corp\. \( guoji shudian \) \.
\. \d{4} chinese academy of sciences \.
\. \d{4} common ground research networks \.
\. \d{4} convivium , association loi de \d{4} \.$
\. \d{4} copyright authors$
\. \d{4} copyright held by the owner / author \( s \) \.
\. \d{4} copyright held by the owner / author \( s \)$
\. \d{4} copyright is held by the owner author \( s \) \.
\. \d{4} corien prins$
\. \d{4} danube adria association for automation and manufacturing , daaam \.
\. \d{4} de silva , burstein , jelinek , stranieri \.$
\. \d{4} dechema e \.
\. \d{4} dei tipografia del genio civile \.
\. \d{4} department of economics , university of calcutta \.
\. \d{4} digital transformation and innovation management \.
\. \d{4} dinabandhu bag \.
\. \d{4} e flow dei tipografia del genio civile \.
\. \d{4} ediciones clio \.
\. \d{4} editions weblaw \.
\. \d{4} editorial board of china offshore oil and gas \.
\. \d{4} editorial department of electric power engineering technology \.
\. \d{4} editorial department of modern electric power \.
\. \d{4} editorial department of resource science \.
\. \d{4} editorial department of zhejiang electric power \.
\. \d{4} edp sciences \.
\. \d{4} edsig \( education special interest group of the aitp \) \.
\. \d{4} educational autonomous non profit organization nephrology \.
\. \d{4} ege universitesi \.
\. \d{4} emerald publishing limited \.
\. \d{4} energy observer magazine co \.
\. \d{4} erp environment and john wiley and sons ltd \.
\. \d{4} estudios de economia aplicada \.
\. \d{4} european council for an energy efficient economy \.
\. \d{4} european safety and reliability association \.
\. \d{4} f \. allen , x \. gu and j \. jagtiani \.$
\. \d{4} faculty of management , warsaw university of technology \.$
\. \d{4} fan , wang , huang , liu and hooten \.$
\. \d{4} financial management association international$
\. \d{4} flacso mexico \.
\. \d{4} franco angeli edizioni \.
\. \d{4} fundacao getulio vargas , escola de direito de sao paulo \.
\. \d{4} fundacao oswaldo cruz \.
\. \d{4} gesellschaft fur informatik \( gi \) \.
\. \d{4} gheorghe asachi technical university of iasi , romania \.
\. \d{4} global energy interconnection group co \. ltd \.$
\. \d{4} growing science ltd \.
\. \d{4} h \. kent baker , greg filbeck and keith black \.
\. \d{4} harris , bonnici , keen , lilaonitkul , white and swanepoel \.$
\. \d{4} hiba alsaidi and david crowther published under exclusive licence by emerald publishing limited \.
\. \d{4} hisin \( history of information systems \) \.
\. \d{4} hongyan li , published by sciendo \.
\. \d{4} human kinetics , inc \.$
\. \d{4} icst institute for computer science , social informatics and telecommunications engineering \.
\. \d{4} iise , incose \.
\. \d{4} incisive risk information \( ip \) limited \.
\. \d{4} infopro digital risk \( ip \) limited \.
\. \d{4} institute for far eastern studies , kyungnam university \.$
\. \d{4} institute of technology and life sciences \( itp \) in falenty \.
\. \d{4} institution of engineering and technology \.
\. \d{4} int \. j \. manag \. bus \. res \.$
\. \d{4} intellect ltd article \.
\. \d{4} international association for computer information systems \.
\. \d{4} international association for housing science \.
\. \d{4} international business information management association \( ibima \) \.
\. \d{4} international conferences e society \d{4} and mobile learning \d{4} \.
\. \d{4} international multidisciplinary scientific geoconference \.
\. \d{4} international strategic management association \.
\. \d{4} issues in information systems \.
\. \d{4} ivan nygaard , et al \.
\. \d{4} iwendi , bashir , peshkar , sujatha , chatterjee , pasupuleti , mishra , pillai and jo \.$
\. \d{4} john wiley and sons , inc \.
\. \d{4} karnov group$
\. \d{4} kelley school of business , indiana university \.
\. \d{4} kelley school of business , indiana university$
\. \d{4} khademi , delir haghighi , lewis , burstein and palmer \.$
\. \d{4} korean distribution science association \( kodisa \) \.
\. \d{4} korean medical association \.
\. \d{4} latin american perspectives , inc \.
\. \d{4} law and development review 2018 \.
\. \d{4} leszek dawid , published by sciendo \.
\. \d{4} li , ma , liao , li , zhu and zhang \.
\. \d{4} lippincott williams and wilkins \.
\. \d{4} llc cpc business perspectives \.
\. \d{4} macmillan publishers limited , part of springer nature \.
\. \d{4} md . faisal faruque et al \.$
\. \d{4} millennial ltd \.
\. \d{4} mohamed k \. hassan et al \.
\. \d{4} natale , paikan , randazzo and domenichelli \.
\. \d{4} nec mediaproducts \.
\. \d{4} nejm catalyst innovations in care delivery \.
\. \d{4} nicholas rosso , philippe giabbanelli \.$
\. \d{4} nova science publishers , inc \.
\. \d{4} owner / author \.$
\. \d{4} pakistan medical association \.
\. \d{4} penerbit akademia baru all rights reserved \.$
\. \d{4} peter lang group ag , lausanne
\. \d{4} pfohl , kim , coan and mitchell \.$
\. \d{4} pijush samui , sanjiban sekhar roy , wengang zhang , and y h taguchi \.
\. \d{4} plant archives \.
\. \d{4} policy studies organization$
\. \d{4} portfolio management research \.
\. \d{4} proceedings of the european conference on management , leadership and governance \.
\. \d{4} publishing house akademperiodyka \.
\. \d{4} publishing house of the higher school of economics \.
\. \d{4} qing ye , jin zhou , hong wu \.$
\. \d{4} regional energy resources information center \( reric \) , asian institute of technology \.
\. \d{4} s \. rasheed et al \.
\. \d{4} s. rasheed et al \.$
\. \d{4} school of law , city university of hong kong \.$
\. \d{4} sciendo \.
\. \d{4} selection and editorial matter , (\b[a-z]+\b\s)+\.
\. \d{4} selection and editorial matter , adriana x \. sanchez , keith d \. hampson and geoffrey london \.
\. \d{4} selection and editorial matter , hemachandran k \. , sayantan khanra , raul v \. rodriguez and juan r \. jaramillo \.
\. \d{4} selection and editorial matter , oscar a \. garcia and prashanth kotturi \.
\. \d{4} selection and editorial matter.*$
\. \d{4} seventh sense research group$
\. \d{4} singleton , noble , sanchez vizcaino , dawson , pinchbeck , williams , radford and jones \.$
\. \d{4} societe francaise de sante publique \.
\. \d{4} society for (\b[a-z]+\b\s)+\.
\. \d{4} society for risk analysis$
\. \d{4} society of chemical industry and john wiley and sons , ltd \. \d{4} society of chemical industry and john wiley and sons , ltd \.
\. \d{4} st \. petersburg state university of architecture and civil engineering \.
\. \d{4} system safety : human technical facility environment \.
\. \d{4} tanushri banerjee , arindam banerjee , dhaval maheta , and vivek gupta \.
\. \d{4} taylor and francis group , london \.$
\. \d{4} tehran urban research and planning center \.
\. \d{4} the american risk and insurance association$
\. \d{4} the association of environmental and resource economists \.
\. \d{4} the author \( s \) , published by de gruyter , berlin / boston \.$
\. \d{4} the author \( s \) \. iet generation , transmission and distribution published by john wiley and sons ltd on behalf of the institution of engineering and technology \.$
\. \d{4} the author \( s \) \. wires energy and environment published by wiley periodicals llc \.
\. \d{4} the author \( s \) \( or their employer \( s \) \) \.
\. \d{4} the authors , faculty of law , masaryk university and ios press \.
\. \d{4} the authors \. intelligent systems in accounting , finance and management published
\. \d{4} the authors disasters \d{4} overseas development institute$
\. \d{4} the authors intelligent systems in accounting , finance and management published by john wiley and sons ltd \.
\. \d{4} the authors wind energy published by john wiley and sons ltd$
\. \d{4} the bank of england$
\. \d{4} the institution of chemical engineers$
\. \d{4} this work is made available under the terms of the creative commons attribution 4\.0 international license , \.
\. \d{4} totem publisher , inc \.
\. \d{4} tu delft \.
\. \d{4} universidade de sao paulo \.
\. \d{4} universidade federal de campina grande \.
\. \d{4} university of california , berkeley \.
\. \d{4} university of florida , fisher school of accounting$
\. \d{4} university of wollongong , faculty of business \.
\. \d{4} valdone darskuviene , nomeda lisauskiene \.$
\. \d{4} verein zur forderung des open access publizierens in den quantenwissenschaften \.
\. \d{4} vestnik sankt peterburgskogo universiteta \. pravo \.
\. \d{4} vilnius gediminas technical university \( vgtu \) press \.$
\. \d{4} volkan , kose , cece and elmas \.$
\. \d{4} walter de gruyter gmbh , berlin / boston \.$
\. \d{4} walter de gruyter gmbh , berlin\/boston \.$
\. \d{4} walter de gruyter inc \.
\. \d{4} wiley periodicals , inc \. complexity
\. \d{4} windeurope \.
\. \d{4} wit press , www \. witpress \. com$
\. \d{4} world federation of orthodontists$
\. \d{4} world regional studies \.
\. \d{4} xlri jamshedpur , school of business management and human resources \.
\. \d{4} zeitschrift fur rechtssoziologie \.
\. \d{4} zemch \.
\. \d{4} zhongguo dianli / electric power \.
\. \d{4} zhongguo dianli/electric power \.
\. \d{4}\. asers publishing \.
\. \d{4}\. los autores \.
\. \d{4}canadian society for civil engineering \.
\. 20th congress of iabse , new york city 2019 : the evolving metropolis report \.
\. a \d{4} pranay gupta and t \. mandy tham \.
\. aarti sathyanarayana , shafiq joty , luis fernandez luque , ferda ofli , jaideep srivastava , ahmed elmagarmid , teresa arora , shahrad taheri \.
\. al$
\. albert park , andrea l hartzler , jina huh , gary hsieh , david w mcdonald , wanda pratt \.$
\. all rights are reserved , including those for text and data mining , ai training , and similar technologies \.$
\. all rights reservwd \.$
\. amaryllis mavragani , alexia sampri , karla sypsa , konstantinos p tsagarakis \.$
\. anna korppoo , iselin stensdal and marius korsnes \d{4} \.
\. aos estratagia and inovacao \.
\. applying artificial intelligence in taiwan fin tech : exploring usage intention of robo advisor service \.
\. arindam brahma , samir chatterjee , kala seal , ben fitzpatrick , youyou tao \.$
\. armand colin \.$
\. arriel benis , nissim harel , refael barak barkan , einav srulovici , calanit key \.$
\. articles the authors$
\. asce , issn \d{4} \d{4} \.
\. asce \.$
\. astes publishers \d{4} \.
\. author \.
\. author \( s \) \( or their employer \( s \) \) \d{4}$
\. author \( s \) \d{4} \.
\. author \( s \) retain copyright ,
\. author$
\. authors \.
\. authors \d{4} \.
\. authors \d{4}$
\. beiesp \.
\. ben glampson , james brittain , amit kaura , abdulrahim mulla , luca mercuri , stephen j brett , paul aylin , tessa sandall , ian goodman , julian redhead , kavitha saravanakumar , erik k mayer \.
\. benjamin l schooley , abdulaziz ahmed , justine maxwell , sue feldman \.$
\. bezhan a \. v. , \d{4} \.$
\. brody foster , matthew david krasowski \.$
\. business strategy and the environment published by erp environment and john wiley and sons ltd \.
\. by the authors \.$
\. caroline strickland , nancy chi , laura ditz , luisa gomez , brittin wagner , stanley wang , daniel j lizotte \.$
\. charlotte havreng thery , arnaud fouchard , fabrice denis , jacques henri veyron , joel belmin \.$
\. chitra lalloo , fareha nishat , william zempsky , nitya bakshi , sherif badawy , yeon joo ko , carlton dampier , jennifer stinson , tonya m palermo \.
\. complexity published by wiley periodicals , inc \.$
\. copy right in bulk will be transferred to ieee by bharati vidyapeeth \.$
\. copyright : \d{4} gudmundarson , peters \.
\. copyright :$
\. copyright \d{4} \[.*\] \.
\. copyright by pacini editore srl$
\. copyright esrel2020 psam15 organizers \.
\. copyright francoangeli \.
\. copyright jes \d{4} on line : journal / esrgroups \. org / jes$
\. copyright jes \d{4} on line : journal/esrgroups.org/jes
\. copyright jes \d{4} on line : journal/esrgroups\.org/jes$
\. copyright nuova cultura \.
\. copyright spie \.
\. copyright the author \( s \) \d{4} \.
\. council of supply chain management professionals$
\. creative commons reconocimiento nocomercial sinobraderivada \.
\. d{4} zeitschrift fur rechtssoziologie \.
\. dalloz \. tous droits reserves pour tous pays \.$
\. datasets : data directly related to this article are provided in the supplementary materials \. dataset license : cc by \d\.0 \.
\. david maddison , katrin rehdanz and heinz welsch \d{4} \.
\. david robert grimes , david h gorski \.$
\. de beaumont foundation \d{4} \.
\. defence research and development canada \.
\. dewi nur aisyah , logan manikam , thifal kiasatina , maryan naman , wiku adisasmito , zisis kozlakidis \.$
\. dialogue \d{4} \. all rights reserved \.$
\. dmitry nikolayev , vinctor sazonov , \d{4} \.
\. downloading of the abstract is permitted for personal use only \.
\. editorial department of electric power construction \.
\. editors and contributors severally \d{4} \.
\. edu \/ journals \.
\. elizabeth heitkemper , scott hulse , betty bekemeier , melinda schultz , greg whitman , anne m turner \.$
\. emerald publishing limited :
\. emergent telemedicine practice in india : challenge and response \.$
\. emmanuel kojo oseifuah , agyapong gyekye , \d{4} \.
\. energy science and engineering published by society of chemical industry and john wiley and sons ltd \.
\. energy science and engineering published by the society of chemical industry and john wiley and sons ltd \.
\. english language \.
\. environmental policy and governance published by erp environment and john wiley and sons ltd \.
\. esrel \d{4} psam15 organizers \.
\. european association of hospital pharmacists \d{4} \.
\. european language resources association \( elra \) , licensed
\. fecap \.
\. felix camirand lemyre , simon levesque , marie pier domingue , klaus herrmann , jean francois ethier \.$
\. for permissions , please email:journals\.permissions@oup\.com \.
\. foreign copyright protection may apply \.
\. from author$
\. from publisher$
\. geografiska annaler : series a , physical geography published by john wiley and sons ltd on behalf of swedish society for anthropology and geography \.
\. gesis \.
\. giulia pullano , lucila gisele alvarez zuzek , vittoria colizza , shweta bansal \.$
\. gka ediciones , authors \.
\. global knowledge academics , authors \.
\. government work and not under copyright protection in the you\.s \.
\. grenze scientific society , \d{4} \.
\. gupta you\. , agarwal b \. , nautiyal n \. , \d{4} \.$
\. hannah r brewer , yasemin hirst , marc chadeau hyam , eric johnson , sudha sundar , james m flanagan \.$
\. henry publications \.
\. hicl \d{4} \.
\. husieva nataliia , niemets oleksii , \d{4} \.
\. iaeme publication scopus indexed$
\. iberamia and the authors \.
\. icis \d{4} \.
\. icope \d{4} \d{1}th international conference on power engineering , proceedings \.
\. iet generation , transmission and distribution published by john wiley and sons ltd on behalf of the institution of engineering and technology \.
\. iet renewable power generation published by john wiley and sons ltd on behalf of the institution of engineering and technology \.
\. iet renewable power generation published by john wiley and sons ltd on behalf of the institution of engineering and technology$
\. ijcesen \.$
\. ijer serials publications \.$
\. in adv neural inf process syst , \d{4} \.
\. individual chapters , the contributors \.
\. individual contributors , their contribution \.
\. individual contributors , their contributions \.
\. infopro digital limited \d{4} \.
\. instytut badan gospodarczych / institute of economic research \( poland \) \.
\. instytut badan gospodarczych \.$
\. integr environ assess manag \d{4}
\. intelligent systems in accounting , finance and management published
\. international building performance simulation association , \d{4}$
\. international research publication house \.
\. ioannis kinias , ioannis tsakalos , nikolaos konstantopoulos , \d{4} \.$
\. it must not be used for commercial purposes \.
\. ivo d \. dinov \d{4} \.$
\. jake luo , guo qiang zhang , susan wentz , licong cui , rong xu \.$
\. jawad chishtie , iwona anna bielska , aldo barrera , jean sebastien marchand , muhammad imran , syed farhan ali tirmizi , luke a turcotte , sarah munce , john shepherd , arrani senthinathan , monica cepoiu martin , michael irvine , jessica babineau , sally abudiab , marko bjelica , christopher collins , b catharine craven , sara guilcher , tara jeji , parisa naraei , susan jaglal \.
\. jiancheng ye , zidan wang , jiarui hai \.$
\. joana m barros , jim duggan , dietrich rebholz schuhmann \.$
\. joseph featherall , brittany lapin , alexander chaitoff , sonia a havele , nicolas thompson , irene katzan \.
\. joshua fuller , alexey abramov , dana mullin , james beck , philippe lemaitre , elham azizi \.$
\. journal of engineering education published by wiley periodicals , inc \. on behalf of asee \.$
\. journal of global business and technology , volume \d{1,3} , number \d{1,3} , spring \d{4} .$
\. julia thomas , antonia lucht , jacob segler , richard wundrack , marcel miche , roselind lieb , lars kuchinke , gunther meinlschmidt \.$
\. kaori kinouchi , kazutomo ohashi \.$
\. karen o'brien and elin selboe \d{4} \.
\. kathryn a riman , billie davis , jennifer b seaman , jeremy m kahn \.$
\. katie allen , nimish valvi , p joseph gibson , timothy mcfarlane , brian e dixon \.$
\. kazuya taira , misa shiomi , takayo nakabe , yuichi imanaka \.$
\. keisuke nakagawa , nuen tsang yang , machelle wilson , peter yellowlees \.$
\. kevin p \. kearns and wenjiun wang \d{4} \.
\. korean distribution science association \( kodisa \) \.
\. korean medical association \.
\. korean medical association$
\. lextenso \. tous droits reserves pour tous pays \.
\. li and li \.
\. li censee mdpi , basel , switzerland \.
\. licensee iust , tehran , iran \.
\. limited liability company$
\. lippincott williams and wilkins \.$
\. little lion scientific \.
\. lizhou fan , lingyao li , libby hemphill \.$
\. madhur thakur , eric w maurer , kim ngan tran , anthony tholkes , sripriya rajamani , roli dwivedi \.$
\. marco lussetti , piper jackson \.
\. mariana traldi , \d{4} and scripta nova \.$
\. matthew spotnitz , john giannini , yechiam ostchega , stephanie l goff , lakshmi priya anandan , emily clark , tamara rlitwin , lew berman \.
\. mayda alrige , riad alharbey , samir chatterjee \.$
\. medical education \.$
\. melinda fitzgerald et al \.
\. michal gaziel yablowitz , sabine dolle , david g schwartz , margitta worm \.$
\. min k chong , ian b hickie , antonia ottavio , david rogers , gina dimitropoulos , haley m lamonica , luke j borgnolo , sarah mckenna , elizabeth m scott , frank iorfino \.
\. mohamed ariff and shamsher mohamad \d{4} \.
\. negar maleki , balaji padmanabhan , kaushik dutta \.$
\. neil jay sehgal , shuo huang , neil mason johnson , john dickerson , devlon jackson , cynthia baur \.$
\. netta shachar , alexis mitelpunkt , tal kozlovski , tal galili , tzviel frostig , barak brill , mira marcus kalish , yoav benjamini \.$
\. nicholas c cardamone , mark olfson , timothy schmutte , lyle ungar , tony liu , sara w cullen , nathaniel j williams , steven c marcus \.
\. nicolas paris , antoine lamer , adrien parrot \.$
\. nileena velappan , ashlynn rae daughton , geoffrey fairchild , william earl rosenberger , nicholas generous , maneesha elizabeth chitanvis , forest michael altherr , lauren a castro , reid priedhorsky , esteban luis abeyta , leslie a naranjo , attelia
\. no commercial re use \.
\. no commercial use is permitted unless otherwise expressly granted \.$
\. nova science publishers , inc \.$
\. onur asan , euiji choi ,$
\. originally published in jmir ai \( http://ai\.jmir\.org \)
\. paul n kizakevich , randall p eckhoff , gregory f lewis , maria i davila , laurel l hourani , rebecca watkins , belinda weimer , tracy wills , jessica k morgan , tim morgan , sreelatha meleth , amanda lewis , michelle c krzyzanowski , derek ramirez , matthew boyce , stephen d litavecz , marian e lane , laura b strange \.
\. penerbit umt \.$
\. penerbit universiti sains malaysia , \d{4} \.
\. peter e lonergan , samuel l washington iii , linda branagan , nathaniel gleason , raj pruthi , peter r carroll , anobel y odisho \.$
\. petersburg state university of architecture and civil engineering \.
\. pin zhong chan , eric jin , miia jansson , han shi jocelyn chew \.$
\. pinku paul , subhajit bhattacharya , \d{4} \.
\. pre results \.
\. preface \.$
\. presses de sciences po \.$
\. proceedings of ecos \d{4} \d{2}th international conference on efficiency , cost , optimization , simulation and environmental impact of energy systems \.
\. production and operations management published by wiley periodicals llc on behalf of production and operations management society \.
\. psychology and marketing published by wiley periodicals llc \.
\. publication rights licensed to acm \.
\. re use permitted under cc by \.
\. re use permitted under cc by nc \.
\. ref \. \d+ , fig \. \d+ \.
\. references \d+ , tables \d+ , fig \. \d+ \.
\. research india publications \.$
\. risk management and insurance review , \d{4}$
\. risk management and insurance review published by wiley periodicals
\. rong yin , katherine law , david neyens \.$
\. sabine baumann \d{4} \.
\. sakun boon itt , yukolpat skunkan \.$
\. sausages \.
\. school of engineering , taylor ' s university \.$
\. see rights and permissions \.
\. seecmar | all rights reserved \.$
\. serials publications pvt . ltd \.
\. seventh sense research group \.$
\. societa editrice il mulino \.
\. society for industrial and organizational psychology \d{4} \.
\. sripriya rajamani , robin austin , elena geiger simpson , ratchada jantraporn , suhyun park , karen a monsen \.$
\. sustainable development published by erp environment and john wiley and sons ltd \.
\. sven festag , cord spreckelsen \.
\. svitlana naumenkova , ievgen tishchenko , volodymyr mishchenko , svitlana mishchenko , \d{4} \.
\. tamkang university , all rights reserved \.$
\. the author \.
\. the author \( \d{4} \) \.
\. the author \( s \) , under exclusive licence to iranian society of environmentalists \( irsen \) and science and research branch , islamic azad university \d{4} \.
\. the author \( s \) under exclusive licence to societa italiana di economia \( italian economic association \) \d{4} \.$
\. the author \d{4} \.
\. the author s \d{4}$
\. the authors , \d{4} \.
\. the authors , publis ad by edp sciences , \d{4} \.
\. the authors , published by edp sciences \.
\. the authors \.
\. the authors published by edp sciences \.
\. the economic history review published by john wiley and sons ltd on behalf of economic history society \.$
\. the editor \( s \) \( ifapplicable \) and the author \( s \) \d{4} \.$
\. the editor and contributing authors severally \d{4} \.
\. the editor and contributors severally \d{4} , international bank for reconstruction and development the world bank \.
\. the editor and contributors severally \d{4} \.
\. the editors and contributors severally \d{4} \.
\. the institution of engineering and technology \.$
\. the institution of engineering and technology$
\. the institution of engineers \( india \) \d{4} \.
\. the research publication \.
\. thieme \.
\. this article is categorized under : wind power > economics and policy \. \d{4} wiley periodicals llc \.
\. this article is categorized under :( ([a-z0-9]+ )+>)+( ([a-z0-9]+ )+\.)
\. this is an open access article under the cc by 4\.0 license \.
\. this open access article is distributed under a creative commons attribution \( cc by \) \d\.0 license \.$
\. this project was funded by the beijing financial fund \.
\. to see the complete license contents \.
\. tubitak \.$
\. tubitak$
\. unep collaborating centre on energy and environme \.
\. universidad del rosario \.$
\. universiti tun hussein onn malaysia publisher ' s office \.$
\. university enterprises cooperation in ukrainian game industry \.$
\. varun k rao , danny valdez , rasika muralidharan , jon agley , kate eddens , aravind dendukuri , vandana panth , maria a parker \.$
\. vilnius university , \d{4} \d{4} \.$
\. wael a \. samad , ahmed badran , and elie azar \d{4} \.
\. wind energy published by john wiley and sons , ltd \.$
\. wind energy published by john wiley and sons ltd \.$
\. wind energy published by john wiley and sons ltd$
\. wires data mining and knowledge discovery published by wiley periodicals llc \.$
\. wires energy and environment published by wiley periodicals llc \.$
\. world scientific publishing co \.
\. world scientific publishing company \.$
\. wydawnictwa uniwersytetu warszawskiego , sekcja wydawnicza wydzialu zarzadzania uniwersytetu warszawskiego , warszawa \d{4} \.
\. wydawnictwa uniwersytetu warszawskiego , sekcja wydawnicza wydziayou zarzadzania uniwersytetu warszawskiego , warszawa \d{4} \.
\. yasmin abdelaal , michael aupetit , abdelkader baggag , dena al thani \.$
\. ye lin , y alicia hong , bradley henson , robert d stevenson , simon hong , tianchu lyu , chen liang \.
\. ying w \.
\. yingzhe yuan , megan price , david f schmidt , merry ward , jonathan nebeker , steven pizer \.$
\. yoonseo park , eun ji kim , sewon park , munjae lee \.$
\. yue tong leung , farzad khalvati \.$
\. zain hussain , zakariya sheikh , ahsen tahir , kia dashtipour , mandar gogate , aziz sheikh , amir hussain \.$
\( \d{4} \) , \( corporacion universitaria lasallista \)
\( \d{4} \) , \( institut za arhitekturu i urbanizam srbije \)
\( \d{4} \) , \( international association of engineers \)
\( \d{4} \) , \( korea information processing society \)
\( \d{4} \) , \( universidad de antioquia \)
\( \d{4} \) , universidad del zulia
\( \d{4} \) (\b[a-z]+\b\s)+publications
\( \d{4} \) (\b[a-z]+\b\s)+publishers
\( \d{4} \) (\b[a-z]+\b\s)+publishing
\( \d{4} \) universidad del zulia
\( american economic association \)
\( cc by 4\.0 \) share adapt
\( international university of sarajevo \)
\( regional inform \. center for sci \. and technol \. \)
\[ figure not available : see fulltext \. \]
\\d{4} antai college of economics and management , shanghai jiao tong university .
\d{2}th european conference on information systems : beyond digitization facets of socio technical change , ecis \d{4}\.
\d{4} , (\b[a-z]+\b\s)*corporacion(\s\b[a-z\+]+\b)*
\d{4} , (\b[a-z]+\b\s)*universidad(\s\b[a-z\+]+\b)*
\d{4} , (\b[a-z]+\b\s)*universitat(\s\b[a-z\+]+\b)*
\d{4} , (\b[a-z]+\b\s)*university(\s\b[a-z\+]+\b)*
\d{4} , (\b[a-z]+\b\s)+publications
\d{4} , (\b[a-z]+\b\s)+publishers
\d{4} , (\b[a-z]+\b\s)+publishing
\d{4} , \( ijacsa \) international journal of advanced computer science and applications \.$
\d{4} , advanced scientific research
\d{4} , american accounting association
\d{4} , american marketing association
\d{4} , association for scientific computing electronics and engineering \( ascee \)
\d{4} , associazione per la matematica applicata alle scienze economiche e sociali \( amases \)
\d{4} , australasian language technology association
\d{4} , bright publisher
\d{4} , cad solutions , llc
\d{4} , central board of irrigation and power
\d{4} , centro de investigacion de la facultad de arquitectura y urbanismo , universidad de cuenca
\d{4} , department for e governance and administration \.
\d{4} , department of languages , literatures , and cultures , mcgill university \.
\d{4} , ediciones clio
\d{4} , editorial(\s\b[a-z\+]+\b)+
\d{4} , el profesional de la informacion
\d{4} , formacion universitaria
\d{4} , formacionuniversitaria
\d{4} , hisin \( history of information systems \)
\d{4} , indian pharmaceutical association
\d{4} , instituto de altos estudios de salud publica
\d{4} , instituto de fisica de liquidos y sistemas biologicos
\d{4} , intellect ltd
\d{4} , international organization on 'technical and physical problems of engineering ' \. all rights reserved \.$
\d{4} , islamic azad university \( iau \)
\d{4} , istituto zooprofilattico dell abruzzo e del molise
\d{4} , ital publication
\d{4} , ital publication \.
\d{4} , journal of(\s\b[a-z\+]+\b)+
\d{4} , kauno technologijos universitetas
\d{4} , korean society of medical informatics
\d{4} , mary ann liebert , inc \. , publishers \.$
\d{4} , omniascience
\d{4} , politechnika lubelska
\d{4} , polska akademia nauk
\d{4} , rev \. mex \. ing \. quimica
\d{4} , revistade la construccion
\d{4} , revistafacultad de ingenieria
\d{4} , revistalasallista de investigacion
\d{4} , scientific publishers of india
\d{4} , society for learning analytics research \( solar \) \. all rights reserved \.$
\d{4} , technical university of liberec
\d{4} , texila international journal \( tij \)
\d{4} , the author
\d{4} , the author \( s \) , under exclusive licence to islamic azad university \.
\d{4} , the institution of engineers \( india \)
\d{4} , the institution of engineers \( india \) \.$
\d{4} , the institution of engineers \( india \)$
\d{4} , universidad del zulia
\d{4} , vldb endowment \.
\d{4} . russian text
\d{4} (\b[a-z]+\b\s)*and(\s\b[a-z]+\b)* \.$
\d{4} (\b[a-z]+\b\s)*corporacion(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*institute(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*instituto(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*universidad(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*universitat(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*universitatii(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*universiti(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)*university(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z]+\b\s)+ association \.
\d{4} (\b[a-z]+\b\s)+council
\d{4} (\b[a-z]+\b\s)+et al
\d{4} (\b[a-z]+\b\s)+meeting
\d{4} (\b[a-z]+\b\s)+publicaciones
\d{4} (\b[a-z]+\b\s)+publications
\d{4} (\b[a-z]+\b\s)+publishers
\d{4} (\b[a-z]+\b\s)+publishing
\d{4} (\b[a-z]+\b\s)+society(\s\b[a-z\+]+\b)*
\d{4} (\b[a-z\+]+\b\s)+journal
\d{4} (\b[a-z\+]+\b\s)+school
\d{4} \. formacion universitaria
\d{4} \. los autores \.
\d{4} \. revistaespacios \. com
\d{4} \d{2}th international conference on efficiency , cost , optimization , simulation and environmental impact of energy systems , ecos \d{4} \.
\d{4} a \. carbone editore
\d{4} a \. massafra et al \.$
\d{4} academic conferences and publishing international limited
\d{4} academy of medical sciences of i \. r \. iran
\d{4} acm
\d{4} african journal of science , technology , innovation and development \.$
\d{4} ais\/icis administrative office
\d{4} alconpat internacional
\d{4} almutairi , almutairi , alhashem and almutairi \.$
\d{4} american academy of ophthalmology$
\d{4} american college of cardiology foundation$
\d{4} american college of radiology$
\d{4} american planning association , chicago , il \.$
\d{4} american psychological association inc
\d{4} american psychological association$
\d{4} american society of civil engineers
\d{4} american society of civil engineers \( asce \)
\d{4} american society of mechanical engineers \( asme \)
\d{4} and scripta nova \.$
\d{4} antai college of economics and management , shanghai jiao tong university \.$
\d{4} article author \( s \) \.$
\d{4} article author \( s \) \( or their employer \( s \) unless otherwise stated in the text of the article \)
\d{4} asce
\d{4} asian research publishing network \( arpn \) \.
\d{4} association for computational linguistics
\d{4} association for computational linguistics \.$
\d{4} association for information systems
\d{4} association of measurement and evaluation in education and psychology \( epodder \)
\d{4} association of researchers in construction management , arcom \d{4} proceedings of the \d{2}th annual conference
\d{4} australian human resources institute \( ahri \)
\d{4} author \( s \) \( or their employer \( s \) \) \.
\d{4} authors \.$
\d{4} azcarate aguerre , den heijer , arkesteijn , vergara d'alencon and klein \.$
\d{4} babatunde omoniyi odedairo , published by sciendo \.
\d{4} berry , moore and ambrose \.$
\d{4} biomed central ltd
\d{4} biondi , caponi , cecere and sciubba \.
\d{4} by (\b[a-z]+\b\s)+
\d{4} by (\b[a-z]+\b\s)+bank
\d{4} by the author(s)?
\d{4} by the authors
\d{4} by the information systems and computing academic professionals , inc \. \( iscap \) \.
\d{4} by the international society of offshore and polar engineers \( isope \) \.
\d{4} canadian association of geographers / l'association canadienne des geographes$
\d{4} china association for science and technology
\d{4} chinese institute of industrial engineers
\d{4} chinese medical association$
\d{4} ciencia , tecnologia y futuro \.$
\d{4} convivium , association loi de \d{4} \d{4} \.$
\d{4} copyright for this paper by its authors
\d{4} copyright held by the owner author \( s \)
\d{4} copyright held by the owner/author \( s \) .
\d{4} copyright held by the owner\/author \( s \)$
\d{4} copyright is held by the owner/author
\d{4} csic consejo superior de investigaciones cientificas
\d{4} dime universita di genova
\d{4} economic society of australia , queensland$
\d{4} ecopetrol s \. a \.
\d{4} editora champagnat
\d{4} editorial board , research of environmental sciences \.
\d{4} editorial office(\s\b[a-z\+]+\b)*
\d{4} elra language resource association
\d{4} elra language resources association
\d{4} elsevier b\.v\. and association of european operational research societies \( euro \)
\d{4} emergency nurses association$
\d{4} estrategia
\d{4} euca
\d{4} european federation for medical informatics \( efmi \)
\d{4} european statistics , windeurope , brussels
\d{4} fintech circle ltd
\d{4} formacion universitaria
\d{4} formisano , vaiano and fabbrocino \.$
\d{4} francesco nocera , et al \.$
\d{4} geology and geophysics institute at azerbaijan national academy of sciences \( anas \)
\d{4} gouveia , seixas , palma , duarte , luz and cavadini \.$
\d{4} held by the owner author \( s \) \.
\d{4} held by the owner/author \( s \) .
\d{4} hellenic association of regional scientists
\d{4} iaeme
\d{4} ieee
\d{4} ieee computer society
\d{4} incoma ltd \.
\d{4} indian drug manufacturers ' association
\d{4} information studies : theory and application
\d{4} informs
\d{4} informs inst \. for operations res \. and the management sciences \.
\d{4} innovative publication , all rights reserved \.
\d{4} institute of industrial engineers \( iie \)
\d{4} institute of physics publishing
\d{4} institution of chemical engineers
\d{4} instituto de altos estudios de salud publica
\d{4} instituto de investigaciones dr \. jose maria luis mora
\d{4} int \. j \. elec \. and elecn \. eng \. and telcomm \.$
\d{4} interciencia
\d{4} international association for mathematics and computers in simulation \( imacs \)
\d{4} international building performance simulation association \( ibpsa \) \.$
\d{4} international energy initiative$
\d{4} international institute for innovation , industrial engineering and entrepreneurship
\d{4} international joint conferences on artificial intelligence \.
\d{4} international medical informatics association \( imia \)
\d{4} is held by the owner author \( s \) \.$
\d{4} jmir public health and surveillance
\d{4} jmir research protocols
\d{4} john wiley and sons ltd
\d{4} journal of management practices , humanities and social sciences \( jmphss \)
\d{4} journal of urban and environmental engineering \( juee \) \.
\d{4} kluwer((, )*\s\b[a-z\+]+\b)*
\d{4} lahore medical and dental college
\d{4} little lion scientific
\d{4} llc ecological help
\d{4} m \. e \. sharpe , inc \.
\d{4} mdpi ag
\d{4} mehdi nourinejad and matthew j
\d{4} mexican society of soil science
\d{4} milbank memorial fund$
\d{4} ministry of health , saudi arabia \.
\d{4} national information and documentation centre
\d{4} niknafs , holmqvist , thollander and rohdin \.
\d{4} nippon telegraph and telephone corp
\d{4} owner author
\d{4} owner/author \.$
\d{4} pan american health organization
\d{4} plos pathogens
\d{4} pontificia universidad javeriana
\d{4} portland international conference on management of engineering and technology , inc \. \( picmet \) \.
\d{4} proceedings \d{2}nd international congress on modelling and simulation , modsim \d{4} \.
\d{4} produccion y limpia
\d{4} pruethsan sutthichaimethee , yothin sawangdee \.$
\d{4} razzaq , amjad , qamar , asim , ishfaq , razzaq and mawra \.$
\d{4} sichuan petroleum administration$
\d{4} sociedad mexicana de ingenieria biomedica
\d{4} society for modeling and simulation international \( scs \)
\d{4} spie
\d{4} taylor and francis
\d{4} taylor and francis group , llc \.$
\d{4} taylor and francis group , london , uk \.
\d{4} tec empresarial
\d{4} telecommunications association inc \. \. all rights reserved \.$
\d{4} terra latinoamericana
\d{4} the american congress of rehabilitation medicine$
\d{4} the association for computational linguistics and chinese language processing \( aclclp \)
\d{4} the author
\d{4} the authors
\d{4} the european federation for medical informatics \( efmi \)
\d{4} the korean society of mineral and energy resources engineers \( ksmer \) \.
\d{4} the korean statistical society , and korean international statistical society
\d{4} troxell , conrad and sussman \.
\d{4} turkish national committee for air pollution research and control$
\d{4} universidad nacional de nordeste ( unne )
\d{4} universidade catolica editora
\d{4} university of split , fesb \.$
\d{4} urban affairs association \.$
\d{4} vilnius gediminas technical university
\d{4} weva page
\d{4} williams , baniassadi , izaga gonzalez , buonocore , cedeno laurent and samuelson \.$
\d{4} world conference(\s\b[a-z\+]+\b)*
\d{4} wydawnictwo sigma not \.
\d{4} yao , shao , yin , wang and lan \.$
\d{4} you \. s \. government \.$
\d{4} zapata riveros , gallati and ulli beer \.
\d{4} zte communications \.
\d{4}mexican society of soil science
2022 wiley vhca ag , zurich , switzerland \.$
a creative commons attribution
a link to the original publication
academy of marketing science
acerca de luz web
advanced science published by wiley vch gmbh \.
aidi italian association of industrial operations professors
alexandru borza botanic garden
all right reserved
all rights are reserved
all rights of reproduction in any form reserved
all rights reserved
all rights reseved
all rigths reserved
american academy of advertising
american college of medical quality \( acmq \) \d{4}
american society for engineering education , \d{4}
american society of civil engineers
americas conference on information systems , amcis
an exclusive publication license$
an imprint of degruyter inc
anales de investigacion en arquitectura
and reproduction in any medium , provided the original work is properly cited
architectural science association \( anzasca \)
article author \( s \) \( or their employer \( s \) unless otherwise stated in the text of the article \)
article s contents are provided on an attribution non commercial
associacao portuguesa para o desenvolvimento regional
associacao portuguesa para o desenvolvimento regional \( apdr \)
associacao sul rio grandense de pesquisadores them historia da educacao
association for information technology trust \d{4} \.
association for the advancement of artificial intelligence \( www \. aaai\.org \) \. all rights reserved \.$
association of military surgeons of the united states \d{4}
attribution 4\.0 international
australis
author \( s \) \( or their employer \( s \) \) \d{4} \.
authors \d{4} \.$
authors retain all copyrights \.$
available for downloading from the publisher
beijing paike culture commu \. co \. , ltd \. \d{4} \.$
by apple academic press , inc \.
by international building performance simulation association \( ibpsa \)
by nc nd 4\.0
by rajbala , pawan kumar singh nain and avadhesh kumar \.$
by scitepress science and technology publications , lda \.
by the electric drive transportation association
by the national athletic trainers ' association , inc \.
by viral hepatitis society
by world scientific publishing co \. pte \. ltd \.
cc by nc nd
cc by nc nd licence
cc by nc nd license
centro de ciencias aplicadas y desarrollo tecnologico
centro de ciencias aplicadas y desarrollo tecnologico$
centro de ciencias$
centro de informacion tecnologica
cerealella
ceur workshop proceedings \( ceur ws \. org \)$
china computer federation \( ccf \) \d{4} \.
chinese optics letters
computational intelligence published by wiley periodicals llc \.
computers and industrial engineering
congress of neurological surgeons \d{4}
content from this work may be used under the terms of the creative commons attribution 3\.0 licence
copying or distributing in print or electronic forms without written permission of igi global is prohibited
copyright : \d{4}(\s\b[a-z\+]+\b)*
copyright \( \d{4} \) by
copyright \d{4}
copyright \d{4}.*\.
copyright \d{4}(\s\b[a-z\+]+\b)*
copyright association of energy engineers \( aee \)
copyright by the paper authors \.$
copyright isca \.$
copyright the author \( s \) , \d{4} \.
copyright the author \( s \) \.$
copyright the authors
corporacion universitaria lasallista \.$
corrected publication \d{4} \.$
creative com mons attribution noncommercial no derivatives 4.0 international license
creative com mons attribution noncommercial no derivatives 4\.0 international licence
creative commons attrib ution noncommercial no derivatives 4\.0 international licence
creative commons attrib ution noncommercial no derivatives 4\.0 international license
creative commons attribu tion noncommercial no derivatives 4\.0 international licence
creative commons attribu tion noncommercial no derivatives 4\.0 international license
creative commons attribution
creative commons attribution non commercial no derivatives \( by nc nd \)
creative commons attribution non commercial no derivatives 4\.0 international licence
creative commons attribution non commercial no derivatives 4\.0 international license
creative commons attribution noncom mercial no derivatives 4\.0 international licence
creative commons attribution noncom mercial no derivatives 4\.0 international license
creative commons attribution noncommercial no derivatives 4\.0 international licence
creative commons attribution noncommercial no derivatives 4\.0 international license
creative commons cc
creative commons international license
creativecommons org licenses
dagmara kociuba , maciej janczak
database url
derechos reservados
derechos reservados \. maracaibo , venezuela
deutsches zentrum fur luft und raumfahrt e \. v \. \d{4} \.$
dhar et al
dimeg university of calabria
distributed under the terms of the creative commons attribution non commercial license
ecos \d{4} \d{2}th international conference on efficency , cost , optimization , simulation and environmental impact of energy systems \.$
ecos \d{4} \d{2}th international conference on efficiency , cost , optimization , simulation and environmental impact of energy systems \.$
editura politechnica
electron \. j \. biotechnol
electron j biotechnol
elfos scientiae
elsevier b \. v
emerald (group )?publishing
escuela de construccion civil
escuela politecnica nacional
este es un articulo de acceso abierto distribuido bajo los terminos de la licencia de uso y distribucion creative commons reconocimiento 4\.0 internacional
este es un articulo en acceso abierto
estoa , \d{4}
eurojournals publishing , inc \. \d{4}
eurojournals publishing inc \d{4}
european , mediterranean and middle eastern conference on information systems , emcis \d{4} \.
european conference on information systems , ecis \d{4} \.
european conference on information systems : beyond digitization facets of socio technical change , ecis \d{4} \.
european conference on management , leadership and governance , ecmlg
european j investiga \.
european management review published by john wiley and sons ltd on behalf of european academy of management \( euram \) \.
evolution and process published by john wiley and sons ltd \.
excelingtech pub
expert systems published by john wiley and sons ltd \.
facultad de ciencias veterinarias
facultad de economia y negocios
facultad(\s\b[a-z\+]+\b)+ \.$
faculty of computer science and information technology
faculty of transport and traffic engineering
for permissions , please email
formacion universitaria all rights reserved
founded by operational programme european fund for regional development of the autonomous province of bolzano efrd 2014-2020 - investments in growth and employment
francesco poletti , marco petrovich , yong chen , greg jasion , eric numkam fokoua , natalie wheeler , tom bradley , hesham sakr , john hayes , ian davidson \d{4} osa \.
from the ministry of science and technology of taiwan \.
fundacao escola de comercio alvares penteado
gazi universitesi muhendislik mimarlik
government employees and their work is in the public domain in the usa \.
harbor , maritime and multimodal logistics modeling and simulation , hms
hemachandran k \. , raul v \. rodriguez , umashankar subramaniam , and valentina emilia balas \.
henry stewart publications
http:// creativecommons
hydrological processes published by john wiley and sons ltd \.
iaeme publication
icis 2022 : " digitization for the next generation "
icst institute for computer sciences , social informatics and telecommunications engineering
ieom society international
ifac \( international federation of automatic control \)
igi global
iise and expo \d{4}
iise annual conference and expo
informa uk limited
inorganic materials : applied research
institut za istrazivanja
institute for transport studies in the european economic integration
institute for transport studies within the european economic integration
institute for transport studies within the european economic integration \( istiee \)
instituto de ciencias aplicadas y tecnologia
instituto tecnologico de costa rica
instytut badan gospodarczych\/institute of economic research \( poland \) \.$
intelligent network and systems society
intelligent transportation systems japan \d{4}
interciencia \d{4}
interciencia association
international association for computer information systems \.$
international association for food protection
international association for management of technology conference , iamot
international association of traffic and safety sciences
international business information management association
international conference on information systems , icis
international conference on information systems , logistics and supply chain
international conference on information systems \d{4} , icis
international conference on sustainability , technology and education \d{4} , ste \d{4} \.
international convention on information and communication technology , electronics and microelectronics
international federation for information processing
international federation of operational research societies
international foundation for autonomous agents and multiagent systems
international information and engineering technology association
international transactions in operational research
international workshop on computer science and engineering
international workshop on computer science and engineering , wcse
iop publishing ltd and sissa medialab
ios press and the authors
ista dyna
italian association for traffic and transport engineering \( aiit \)
japan association of mineralogical sciences$
japan industrial management association
john wiley and sons , ltd
john wiley and sons ltd
journal of management practices , humanities and social sciences
journals \. permissions@oup \. com \.
jurnal penelitian psikologi
kedge bs
kluwer law international bv , the netherlands
kluwer law international bv , the netherlands \.$
latin american center for informatics studies
learning health systems published by wiley periodicals
learning health systems published by wiley periodicals llc on behalf of university of michigan \.
lecture notes in computer science
leontyeva yu
licensee : aosis
licensee : revista ingenieria
licensee cogitatio \( lisbon , portugal \) \.$
licensee mdpi , basel , switzerland
licensee(\s\b[a-z\+]+\b)+
liver international published by john wiley and sons ltd \.$
lulea university of technology , sweden \.
lulea university of technology , sweden \.$
lulea university of technology , sweden \d{4}\.
mary ann liebert , inc \.$
mexican society of soil science
muhammad ali memon , mohamed hedi karray , agnes letouzey and bernard archimede \. published by emerald publishing limited .
national academy of sciences
national university of singapore , faculty of law \.
networks published by
networks published by wiley periodicals llc
neural information processing systems foundation
nutrition bulletin published by john wiley and sons ltd on behalf of british nutrition foundation
on behalf of british educational research association
on behalf of policy studies organization \.$
on behalf of teaching statistics trust \.$
on behalf of the institution of engineering and technology \.$
on behalf of the university of michigan$
onyshchenko v \. o\. , zavora t \. m\. , filonych o \. m\. , \d{4} \.$
operational research society \d{4}
operations and supply chain management forum
orientalis \. \d{4}$
originally published in jmir formative research
pacific asia conference on information systems : information systems \( is \) for the future
peer review under responsibility of the scientific committee of icae\d{4} the \d{2}th international conference on applied energy \.$
peer review under responsibility of the scientific committee of the \d{1,2}th international symposium intelligent systems
personal use is permitted , but republication/redistribution requires ieee permission \.
plea conference on passive and low energy architecture planning post carbon cities , proceedings \.
pleiades publishing , ltd \.
pontificia universidad catolica de valparaiso
pontificia universidad javeriana
proceedings of the \d{2}rd pacific asia conference on information systems : secure ict platform for the 4th industrial revolution
proceedings of world multi conference on systemics , cybernetics and informatics , wmsci
proceedings of(\s\b[a-z0-9\+]+\b)+
prospero \( registration number
prospero registration number
prospero registration number crd42020196473 \.
provided the original author and source are credited
publication rights licensed to association for computing machinery \.$
published by brian towers \( britow \) and john wiley and sons ltd \.
published by reric in international energy journal \( iej \) \.
published by the vinca institute of nuclear sciences , belgrade , serbia \.$
published by(\s\b[a-z \+]+\b)+
published in (\b[a-z]+\b\s)*, \d{4}
published under a creative commons attribution licence \.$
published under exclusive licence by
published under licence by (\b[a-z]+\b\s)*
published under license by (\b[a-z]+\b\s)*
published with(\s\b[a-z\+]+\b)+
ram arti publishers \.$
re use permitted under cc by nc \.$
readers are allowed to copy , distribute and communicate article s contents , provided the author s and intangible capital s names are included
real estate economics published
reproduction right holder
reprodution right holder universidad distrital franciso jose de caldas
reprodution right holder universidad distrital franiso jose de caldas
research synthesis methods published by john wiley and sons ltd \.
review of policy research published by wiley periodicals
revista cientifica de la facultad de veterinaria
revista de la construccion
revista dyna
revista facultad de ingenieria
revista facultad de ingenieria , universidad de antioquia
revista ingenieria e investigacion editorial board
roceedings of the 17th international symposium on operational research in slovenia , sor \d{4}
roduction and operations management society
sas institute , inc \.
science and information organization
scientia sinica informationis
selection and editorial matter
series c \( applied statistics \) published by john wiley and sons ltd on behalf of royal statistical society$
series c \( applied statistics \) published by john wiley and sons ltd on behalf of the royal statistical society \.
series transport
shehab et al
sila science
sociedade brasileira de quimica
society for imaging informatics in medicine \d{4} , \d{4} \.
society for imaging informatics in medicine 2010\.2021 \.$
society of petroleum engineers
some right reserved
some rights reserved
some rights reseved
some rigths reserved
springer international publishing switzerland \d{4} \.$
submitted for possible open access publication
svitlana naumenkova , ievgen tishchenko , volodymyr mishchenko , svitlana mishchenko , \d{4} \.$
taiwan academic network management committee
taiwan association for aerosol research \.$
technical committee on control theory , chinese association of automation \.$
tecnologia y ciencias del agua \.$
the architectural science association and griffith university , australia \.$
the author \( s \)
the authors , \d{4} \.$
the authors , published by edp sciences
the brazilian society of mechanical sciences and engineering
the cotton foundation \d{4}
the creative commons attribution license
the creative commons cc by license
the division of operation and maintenance , lulea university of technology
the editor \( s \)
the institution of engineering and technology \d{4}
the japanese society of nuclear medicine \d{4} \.
the national bureau of asian research
the online demo is available at
the society for reliability engineering , quality and operations management \( sreqom \) , india
the terms and conditions of the creative commons attribution
the views represented in the paper do not necessarily represent the views of the institutions or of all the co authors \.$
the youtube link of the full recorded interview can be accessed at
this article also appears , with a number of url links , on the biopharm web site
this article is categorized under : application areas > health care \. 2021 wiley periodicals llc \.
this article is distributed under the terms of the creative commons atribution 4\.0 internacional licence
this article is distributed under the terms of the creative commons atribution 4\.0 internacional license
this book is an open access publication
this copyright and license information must be included \.$
this is an open access article
this is an open access article distributed under the terms of
this is an open access article under the cc by sa license
this open access article is distributed under a creative commons attribution
this research granted the \d{4} award of the cuban national academy of sciences
this work granted the annual award of the national academy of sciences of cuba for the year
this work is distributed under the creative commons attribution 4\.0 license
this work is licenced under
this work is licensed under
this work is licensed under a creative commons attribution noncommercial noderivatives 4\.0 international license \.
this work is written by us government employees and is in the public domain in the us \.$
to see the complete license contents
transportation research board
trial registration number
trial registration:clinicaltrials\.gov
trial registration:clinicaltrials\.gov id
tsenov academy of economics
tut badan gospodarczych institute of economic research \( poland \) \.
under exclusive licence to
under exclusive licence to european association for predictive , preventive and personalised medicine \( epma \)
under exclusive licence to german academic society for production engineering \( wgp \)
under exclusive licence to international center for numerical methods in engineering \( cimne \)
under exclusive licence to iranian society of environmentalists \( irsen \) and science and research branch , islamic azad university \.$
under exclusive licence to iranian society of environmentalists \( irsen \) and science and research branch , islamic azad university \d{4} \.
under exclusive licence to shiraz university \.$
under exclusive licence to shiraz university \d{4} \.$
under exclusive licence to sociedade brasileira de matematica aplicada e computacional
under exclusive license to
under the creative commons attribution noncommercial noderivs
under the terms and conditions of the creative commons attribution \( cc by \) license
universidad alberto hurtado
universidad de antioquia \.$
universidad del zulia
universidad del zulia \d{4} , derechos reservados . maracaibo , venezuela
universidad distrital francisco jose de caldas
universidad nacional de colombia
universidad ort uruguay \.
university of birmingham
university of cienfuegos , carlos rafael rodriguez
upon the material in any medium so long as the original work is properly cited \.
use permitted under creative commons license attribution
vaginalis \. \d{4}$
vilnius gediminas technical university \( vgtu \)
which permits unlimited use , distribution and reproduction in any medium so long as the original work is properly cited \.
which permits unrestricted use , distribution , and reproduction in any medium
which permits unrestricted use distribution and reproduction in any medium
wiley blackwell
wiley periodicals
with in the international federation of operational research societies \( ifors \)
wolters kluwer health , inc \.
world academic union
world advertising research center
world health organization 2015
world multi conference on systemics , cybernetics and informatics , proceedings
world scientific and engineering academy and society
www : biopharm mag . com
www : biopharm mag com \.
wydawnictwo ekonomia i srodowisko
xiang t \. r \. kong , ray y \. zhong , gangyan xu and george q \. huang \. published by emerald publishing limited \.
""".split(
            "\n"
        ),
        key=lambda line: len(line.split(" ")),
        reverse=True,
    )
)
