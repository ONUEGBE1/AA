# ⌯ Hey, Bro This File Code By : Carlo
# ⌯ Syntx : Python3
# ⌯ This File Is Free !!
# ⌯ Devlloper Channel : @IHFIH
# ⌯ Thanks You Bro Enjoy
#============================#

# The Api : https://psksks.tk/Api/Combo.php From Trakos ! 
try:
	import random,os,pyfiglet,requests
except Exception as Carlo:exit(Carlo)
chars=['eya', 'ahmed', 'mariem', 'firas', 'ghada', 'mohamed', 'rania', 'aziz', 'emna', 'mehdi', 'cyrine', 'sami', 'sarah', 'yassine', 'fatma', 'amine', 'salma', 'karim', 'malek', 'med', 'sarra', 'aymen', 'wafa', 'mohamed', 'yosr', 'ali', 'erij', 'ayoub', 'imen', 'adam', 'mel', 'khalil', 'ghofrane', 'khaled', 'khouloud', 'hamza', 'hiba', 'rayen', 'amani', 'sara', 'marwen', 'ines', 'omar', 'rihab', 'houssem', 'dhifef', 'ibrahim', 'esra', 'hani', 'maram', 'marouen', 'nesrine', 'alaa', 'syrine', 'hedy', 'yasmine', 'taha', 'sana', 'oussama', 'chaima', 'atef', 'nour', 'ghaith', 'safa', 'brice', 'ramla', 'skander', 'chourouk', 'radhi', 'nadia', 'chokri', 'kenza', 'monem', 'khadija', 'hichem', 'aya', 'helmi', 'asma', 'taher', 'mariam', 'slim', 'melek', 'akram', 'soulayma', 'azer', 'hana', 'achraf', 'arij', 'adem', 'ons', 'dhia', 'hend', 'fabrice', 'yosra', 'qayes', 'wided', 'anas', 'sabrine', 'sahar', 'abdou', 'meriam', 'mouadh', 'maya', 'wilfried', 'aicha', 'nick', 'myriam', 'taysir', 'marie', 'mhaddeb', 'rahma', 'ismail', 'oumaima', 'gorge', 'lyna', 'noufèl', 'farah', 'oussama', 'lilia', 'mongi', 'nada', 'cyrille', 'abir', 'hakim', 'souhaïla', 'fourat', 'sirine', 'dora', 'souhail', 'aycha', 'ramy', 'ele', 'soufiane', 'yesmine', 'hazem', 'naziha', 'jilani', 'yang', 'heithem', 'souad', 'borgia', 'mia', 'mahdi', 'omayma', 'hakima', 'shayma', 'moussa', 'nouha', 'valls', 'jey', 'claudio', 'bochra', 'jess', 'hizo', 'wrynn', 'mahjbi', 'sanda', 'majda', 'ghaya', 'yahya', 'sebai', 'malek', 'napathy', 'mohanned', 'lia', 'midou', 'meri', 'osman', 'ojo', 'cherif', 'lilly', 'moha', 'kallala', 'steve', 'amira', 'thierry', 'sihem', 'innocent', 'malek', 'dali', 'olfa', 'idris', 'mary', 'iheb', 'wissal', 'chaabane', 'faneva', 'jamel', 'zahra', 'houcine', 'habiba', 'hafsi', 'amèni', 'trabelsi', 'gigi', 'melek', 'amena', 'burhan', 'maya', 'sydu', 'suske', 'uri', 'maen', 'ranim', 'mohammed', 'haya', 'usama', 'ousa', 'joram', 'sandra', 'nizar', 'rojda', 'rifat', 'souzan', 'hady', 'ñàw', 'elias', 'qamar', 'rosarita', 'hasan', 'hala', 'akram', 'sara', 'ali', 'layal', 'zak', 'reem', 'miran', 'zain', 'hayyan', 'sara', 'david', 'megan', 'klajdi', 'ana', 'hoohi', 'fiona', 'albert', 'seddjjk', 'stanley', 'sidorela', 'adam', 'aeg', 'bam', 'luvas', 'jenny', 'shi', 'klea', 'klaus', 'tammy', 'zeph', 'elsjana', 'nick', 'saveliy', 'ann', 'jack', 'selena', 'vinski', 'skittels', 'asd', 'arnisa', 'valmir', 'anja', 'diellor', 'deborah', 'riad', 'zia', 'jean', 'roslyn', 'daniel', 'han', 'flavio', 'dea', 'chang', 'nihada', 'lukas', 'adriana', 'fatlind', 'eria', 'kevin', 'arlinda', 'rrezon', 'midori', 'fatjon', 'tahrijah', 'arti', 'diana', 'desiree', 'getoard', 'megumi', 'zygmund', 'aksa', 'maltin', 'koranfo', 'sara', 'david', 'megan', 'klajdi', 'ana', 'hoohi', 'fiona', 'albert', 'seddjjk', 'stanley', 'sidorela', 'adam', 'aeg', 'bam', 'luvas', 'jenny', 'shi', 'klea', 'klaus', 'tammy', 'zeph', 'elsjana', 'nick', 'saveliy', 'ann', 'jack', 'selena', 'vinski', 'skittels', 'asd', 'arnisa', 'valmir', 'anja', 'diellor', 'deborah', 'riad', 'zia', 'jean', 'roslyn', 'daniel', 'han', 'flavio', 'dea', 'chang', 'nihada', 'lukas', 'adriana', 'fatlind', 'eria', 'kevin', 'arlinda', 'rrezon', 'midori', 'fatjon', 'tahrijah', 'arti', 'diana', 'desiree', 'getoard', 'megumi', 'zygmund', 'aksa', 'maltin', 'koranfo', 'galy', 'charles', 'andrea', 'jalen', 'samara', 'javon', 'justine', 'anthony', 'gracie', 'kendall', 'anita', 'andres', 'renessa', 'chad', 'dawnie', 'jordan', 'clinton', 'marie', 'clivon', 'taja', 'laquan', 'gina', 'louvens', 'isabelle', 'lukas', 'sanyjah', 'vaughn', 'deja', 'kent', 'garbriel', 'antonio', 'ledeja', 'jahni', 'emma', 'kevin', 'marge', 'fred', 'jessica', 'kevon', 'drea', 'kenton', 'ural', 'ashley', 'ramon', 'denesha', 'jarrette', 'alexis', 'richard', 'kaielle', 'mateo', 'lennisha', 'jayden', 'jasmine', 'aiden', 'chrishan', 'sashm', 'tay', 'abby', 'peter', 'dani', 'erris', 'kaylyn', 'deshawn', 'azariah', 'thompson', 'rhyse', 'stacie', 'desaray', 'hope', 'charlee', 'jaquell', 'star', 'tom', 'khylie', 'jodi', 'kia', 'darshan', 'arianna', 'tammy', 'seaneka', 'nevaeh', 'olujinmi', 'eliana', 'isadora', 'randisha', 'arrianna', 'katie', 'camila', 'franco', 'sofia', 'matias', 'victoria', 'joaquín', 'agustina', 'martín', 'paula', 'juan', 'julieta', 'mauro', 'micaela', 'ignacio', 'ana', 'federico', 'lucas', 'maria', 'santiago', 'natalia', 'pablo', 'daiana', 'laura', 'nicolas', 'lucia', 'benjamin', 'juana', 'tomas', 'carolina', 'marcos', 'andrea', 'fernando', 'ezequiel', 'martina', 'facundo', 'michelle', 'ilan', 'flavia', 'daniel', 'milagros', 'gabriel', 'evelyn', 'agustin', 'pedro', 'sandra', 'javier', 'noelia', 'isaias', 'sol', 'faustino', 'catalina', 'fabricio', 'belen', 'valentin', 'abril', 'manuel', 'candela', 'alex', 'rocio', 'gonzalo', 'eliana', 'ian', 'mariana', 'juan', 'verónica', 'fabian', 'cecilia', 'mateo', 'tatiana', 'thomas', 'daniela', 'gregorio', 'mary', 'sergio', 'nadia', 'david', 'luz', 'thiago', 'ingrid', 'guido', 'cintia', 'lautaro', 'lara', 'leandro', 'rebeca', 'aaron', 'romina', 'uziel', 'clara', 'araceli', 'edgardo', 'magali', 'josef', 'zoe', 'jacobo', 'brenda', 'rafael', 'ileana', 'benjamin', 'marina', 'justin', 'tania', 'emilio', 'karina', 'misael', 'virginia', 'tobias', 'milena', 'luciano', 'nerea', 'michael', 'silvina', 'coti', 'paz', 'jutice', 'celeste', 'max', 'lola', 'eduardo', 'aldana', 'hari', 'gabriela', 'nahuel', 'juliana', 'rafa', 'leo', 'valeria', 'alexis', 'steffy', 'macarena', 'name', 'gisela', 'patrick', 'ayelén', 'tadeo', 'ona', 'milco', 'melisa', 'jorge', 'melina', 'victor', 'julia', 'anthonny', 'elena', 'moshe', 'noe', 'mijael', 'angie', 'medi', 'harry', 'malena', 'ruben', 'mariela', 'aaron', 'caro', 'alan', 'anna', 'taedio', 'abigail', 'merleau', 'emilia', 'piere', 'melany', 'darío', 'yael', 'hugo', 'eugenia', 'yuliza', 'patricia', 'paul', 'mora', 'jasmin', 'magt', 'mauricio', 'lorena', 'mara', 'diego', 'nancy', 'andy', 'ivana', 'leandro', 'agostina', 'rodri!', 'meli', 'enrique', 'paulina', 'gastón', 'johanna', 'kross', 'kilian']
chars1 = (("0987654321")); chars2=(("azertyuiopqsdfghjklmwxcvbn"));total=0
class saud1:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(7)));self.num= '+96650'+self.numb;self.pasw='050'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class saud2:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(7)));self.num= '+96653'+self.numb;self.pasw='053'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class saud3:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(7)));self.num= '+96655'+self.numb;self.pasw='055'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
		
class algeria:
	def __init__(self):
		self.algeria=sk("Algreia");os.system('clear');echo(self.algeria);echo(""+W+"=======================================");echo(f"{R}[{G}1{R}]{W} 077\n{R}[{G}2{R}]{W} 067\n{R}[{G}3{R}]{W} 055");self. choser2=input(f"{R}[{G}${R}]{W} Chose One :{P}");
		if self.choser2=="1":alger1()	
		if self.choser2=="2":alger2()
		if self.choser2=="3":alger3()
class cho:
	def __init__(self, choser):
		if choser == "1":Combo_Mail(chars, dom)
		if choser == "2":Combo_Number(chars1) 
		if choser == "3":Combo_User()
		if choser == "4":exit
class start:
	def __init__(self):
		echo(""+W+"===============================");echo(f"{R}[{G}1{R}]{W} Combo Mails ");echo(f"{R}[{G}2{R}]{W} Combo Numbers ");echo(f"{R}[{G}3{R}]{W} Combo Users");echo(f"{R}[{G}4{R}]{W} Exit");echo(""+W+"===============================");choser = input(f"{R}[{G}${R}]{W} Chose One :{P}");cho(choser)
class saudia:
	def __init__(self):
		self.saudia=sk("Saudia");os.system('clear');echo(self.saudia);echo(""+W+"=======================================");echo(f"{R}[{G}1{R}]{W} 050\n{R}[{G}2{R}]{W} 053\n{R}[{G}3{R}]{W} 055");self. choser2=input(f"{R}[{G}${R}]{W} Chose One :{P}");
		if self.choser2=="1":saud1()
		if self.choser2=="2":saud2()
		if self.choser2=="3":saud3()
class iq1:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(8)));self.num= '+96477'+self.numb;self.pasw='077'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class iq2:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(8)));self.num= '+96478'+self.numb;self.pasw='078'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class eg1:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(8)));self.num= '+2010'+self.numb;self.pasw='010'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class eg2:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(8)));self.num= '+2011'+self.numb;self.pasw='011'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class eg3:
	def  __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(8)));self.num= '+2012'+self.numb;self.pasw='012'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class iq3:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(8)));self.num= '+96475'+self.numb;self.pasw='075'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
				
class Combo_Mail:
			def __init__(self, chars, dom):
				global total
				count=input(f"{R}[{G}={R}]{W} Send The Count Of Combo : ")
				pasw = "1122334455" , "1234512345" , "11223344" , "0000" , "19981998" , "19901990"
				self.count=int(count)
				for y in range(self.count):
					self.total=total;self.chars1=chars1;self.name = str("". join(random.choice(chars)for i in range(1)));self.pasw=random.choice(pasw);self.domain = str("". join(random.choice(dom)for i in range(1)));self.number = str("". join(random.choice(self.chars1)for i in range(3)));self.mail = self.name+self.number+self.domain;total+=1
					with open("Combo.txt", "a")as kimo:kimo.write(f"{self.mail}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class iraq:
	def __init__(self):
		self.iraq=sk("Iraq");os.system('clear');echo(self.iraq);echo(""+W+"=======================================");echo(f"{R}[{G}1{R}]{W} 077\n{R}[{G}2{R}]{W} 078\n{R}[{G}3{R}]{W} 075");self. choser2=input(f"{R}[{G}${R}]{W} Chose One :{P}");
		if self.choser2=="1":iq1()
		if self.choser2=="2":iq2()
		if self.choser2=="3":iq3()
class alger1:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(7)));self.num= '+21377'+self.numb;self.pasw='077'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class egypt:
	def __init__(self):
		self.egypt=sk("Egypt");os.system('clear');echo(self.egypt);echo(""+W+"=======================================");echo(f"{R}[{G}1{R}]{W} 010\n{R}[{G}2{R}]{W} 011\n{R}[{G}3{R}]{W} 012");self. choser2=input(f"{R}[{G}${R}]{W} Chose One :{P}");
		if self.choser2=="1":eg1()
		elif self.choser2=="2":eg2()
		elif self.choser2=="3":eg3()
class alger2:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(7)));self.num= '+21367'+self.numb;self.pasw='067'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class alger3:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
			self.chars1=chars1;self.numb = str("". join(random.choice(self.chars1)for i in range(7)));self.num= '+21355'+self.numb;self.pasw='055'+self.numb;self.total+=1
			with open("Combo.txt", "a")as kimo:kimo.write(f"{self.num}:{self.pasw}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
class Combo_Number:
	
	def __init__(self, chars1):
		global total
		self.chars1=chars1;echo(f"{R}[{G}1{R}]{W} Combo Algeria\n{R}[{G}2{R}]{W} Combo Saudia\n{R}[{G}3{R}]{W} Combo Iraq\n{R}[{G}4{R}]{W} Combo Egypte");echo(""+W+"===============================");self.choser_=input(f"{R}[{G}${R}]{W} Chose One :{P}")
		if self.choser_=="4":egypt()
		if self.choser_=="3":iraq()
		if self.choser_=="2":saudia()
		if self.choser_=="1":algeria()
		
		
class Combo_User:
	def __init__(self):
		count=input(f"{R}[{G}={R}]{W} Send The Count Of The Combo : ");self.count=int(count);self.total=total
		for y in range(self.count):
		 	api = requests.get('https://psksks.tk/Api/Combo.php').json()
		 	self.user= api['User']
		 	self.ps = api['Pass']
		 	with open("Combo.txt", "a")as kimo:kimo.write(f"{self.user}:{self.ps}\n");echo(f'\r{G}[+] Total : {self.total}', end="")
		 		
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
B="\033[2;32m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
echo=print
dom="@gmail.com","@yahoo.com","@hotmail.com","@live.com","@mail.ru"
sk = pyfiglet.figlet_format
if  __name__ == "__main__":
	start()	