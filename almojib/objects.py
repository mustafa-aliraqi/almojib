class user:
	def __init__(self,json):
		self.json = json
	@property
	def userId(self):
		self.users = []
		for user in self.json:
			self.users.append(user["user"]["id"])
		return self.users
	@property
	def nickname(self):
		self.Names = []
		for name in self.json:
			self.Names.append(name["user"]["display_name"])
		return self.Names
	@property
	def age(self):
		self.Ages =[]
		for Age in self.json:
			self.Ages.append(Age["user"]["age"])
		return self.Ages
	@property
	def gender(self):
		self.genders = []
		for gen in self.json:
			self.genders.append(gen["user"]["gender"])
		return self.genders
	@property
	def country(self):
		self.countrys = []
		for cou in self.json:
			self.countrys.append(cou["user"]["country"]["name"])
		return self.countrys
	@property
	def countryId(self):
		self.countrysId= []
		for cou in self.json:
			self.countrysId.append(cou["user"]["country"]["id"])
		return self.countrysId
class search:
	def __init__(self,json):
		self.json = json
	@property
	def subject(self):
		self.Subject = self.json["outcome"]["data"]
		self.SubjectList = []
		for subj in self.Subject:
			self.SubjectList.append(subj["question"]["subject"])
		return self.SubjectList
	@property
	def score(self):
		self.Score = self.json["outcome"]["data"]
		self.ScoreList = []
		for kj in self.Score:
			self.ScoreList.append(kj["question"]["score"])
		return self.ScoreList
	@property
	def message(self):
		self.Msg = self.json["message"]
		return self.Msg
	@property
	def question(self):
		self.Question = self.json["outcome"]["data"]
		self.QuestionList = []
		for ques in self.Question:
			self.QuestionList.append(ques["question"]["question"])
		return self.QuestionList
	@property
	def answer(self):
		self.Answer = self.json["outcome"]["data"]
		self.AnswerList = []
		for ans in self.Answer:
			self.AnswerList.append(ans["first_reply"]["reply"])
		return self.AnswerList
	@property
	def questionId(self):
		self.QuestionId = self.json["outcome"]["data"]
		self.QuestionIdList=[]
		for queid in self.QuestionId:
			self.QuestionIdList.append(queid["question"]["id"])
		return self.QuestionIdList
	@property
	def answerId(self):
		self.AnswerId = self.json["outcome"]["data"]
		self.AnswerIdList = []
		for AnsId in self.AnswerId:
			self.AnswerIdList.append(AnsId["first_reply"]["id"])
		return self.AnswerIdList
	@property
	def author(self):
		self.Author = self.json["outcome"]["data"]
		return user(self.Author)