pragma solidity^0.4.11;

contract Survey{
	struct ShareHolder {
		address addr;
	}
	
	struct Voter {
		address addr;
		bool voted;
		uint answer;
	}
	
	struct Question {
		uint id;
		string description;
		bool isopen;
		Voter[] voters;
	}
	
	uint questionCounter;
	address public director;
	mapping (uint => Question) public questions;
	mapping (address => ShareHolder) public shareholders;

	//constructor
	function Survey(address[] shareholderAddress) public {
		// set owner
		director = msg.sender;
		
		//create shareholders
		for (uint i = 0; i < shareholderAddress.length; i++) {
			shareholders[shareholderAddress[i]].addr = shareholderAddress[i]; 
        }
	}
	
	// set modifier which will be applied on several functions
	modifier onlyDirector {
        require(msg.sender == director);
        _;
    }
	
	// create question
	function createQuestion(string questiondescription) onlyDirector private {
		uint questionID = questionCounter++;
		questions[questionID].id = questionID;
		questions[questionID].description = questiondescription;
		questions[questionID].isopen = true;
	}
	
	//add shareholder to the list of voters
	function addVoterIntoQuestion(address voteraddress, uint questionid) onlyDirector  private {
		require(questions[questionid].isopen);
		ShareHolder shareholder = shareholders[voteraddress];
		if (voteraddress != director){
			questions[questionid].voters.push(Voter({addr:shareholder.addr,voted:false,answer:0}));
		}
	}
	
	//remove shareholder from the list of voters
	function removeVoterFromQuestion(address voteraddress, uint questionid) onlyDirector private {
		require(questions[questionid].isopen);
		
		ShareHolder shareholder = shareholders[voteraddress];
		bool found = false;
		uint tempidx = 0; 
		for (uint i=0; i< questions[questionid].voters.length; i++){
			if (questions[questionid].voters[i].addr == shareholder.addr){
				found = true;
				tempidx = i;
				break;
			}
		}
		
		if(found){
			delete questions[questionid].voters[tempidx];
		}		
	}
	
	// close voting
	function closeVoting(uint questionid) onlyDirector private {
		require(questions[questionid].isopen);
		questions[questionid].isopen = false;
	}
	
	
	// give a vote
	function vote(uint questionid, uint answer) public {
		address sender = msg.sender;
        Question storage question = questions[questionid];	
		
		//check if sender is not director and question is still open
		require(sender != director);
		require(question.isopen);
		
		for (uint i=0; i<question.voters.length; i++){
			// if shareholder in the list of voters and he has not voted yet, then allow them to vote
			if (question.voters[i].addr == sender && !question.voters[i].voted){
				questions[questionid].voters[i].answer = answer;
				questions[questionid].voters[i].voted = true;
				break;
			}
		}
    }
	
	//majority decision
	function majorityDecision(uint questionid) public view returns (uint majorityanswer)
    {
		address sender = msg.sender;
		Question storage question = questions[questionid];	
		bool isabletoseetheresult = false;
		
		//director can see the result any moment
		if (sender == director){
			isabletoseetheresult = true;
		}
		else {
			// shareholders can see the result after the voting is closed
			if (!question.isopen){
				isabletoseetheresult = true;
			}	
		}
		
		if (isabletoseetheresult){
			uint agree = 0;
			uint notagree = 0 ;

			for (uint i = 0; i < questions[questionid].voters.length; i++) {
				if (questions[questionid].voters[i].voted) {
				   if (questions[questionid].voters[i].answer == 0){
						notagree = notagree + 1;
				   }
				   else {
						agree = agree + 1;
				   }
				}
			}

			if (agree > notagree){
				majorityanswer = 1;
			}
			else {
				majorityanswer = 0;
			}
		}
	}
}