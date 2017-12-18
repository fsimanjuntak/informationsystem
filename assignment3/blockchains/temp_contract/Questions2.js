pragma solidity^0.4.11;

contract {
	struct ShareHolder {
		address addr;
		bool isallowedtovote;
	}
	
	struct Voter {
		address addr;
	}
	
	struct Question {
		uint id;
		string description;
		boolean isopen;
		uint totalcountagree;
		uint totalcountdisagree;
		maSurveypping (address => Voter) voters;
	}
	
	uint questionCounter;
	address public director;
	mapping (uint => Question) public questions;
	mapping (addr => ShareHolder) public shareholders;
	
	
	// constructor
	function Survey(address[] shareholderNames) public {
		// set owner
		director = msg.sender;
		
		//create shareholders
		for (uint i = 0; i < shareholderNames.length; i++) {
            shareholders.push(ShareHolder({
                addr: shareholderNames[i],
                isallowedtovote: false
            }));
        }
	}	
	
	// create question
	function createQuestion(string questiondescription) private {
		require(msg.sender == director);
		questionID = questionCounter++;
		questions.push(Question(questionID,questiondescription,true,0,0,[]));
	}
	
	// enable shareholder to vote
	function enableVoterToAnswerQuestions(address voteraddress) private{
		require(msg.sender == director);
		shareholders[voteraddress].isallowedtovote = true;
	}
	
	// disable shareholder to vote
	function disableVoterToAnswerQuestions(address voteraddress) private{
		require(msg.sender == director);
		shareholders[voteraddress].isallowedtovote = false;
	}
	
	// close voting
	function closeVoting(uint questionid) private{
		require(msg.sender == director);
		require(question.isopen);
		questions[questionid].isopen = false;
	}
	
	// give a vote
	function vote(uint questionid, uint answer) public {
		address sender = msg.sender;
		ShareHolder shareholder = shareholders[sender];
        Question storage question = questions[questionid];	
		
		//check if sender is not director, sender is allowed to vote, and question is still open
		require(sender != director);
		require(shareholder.isallowedtovote);
		require(question.isopen);
		
		//check whether shareholder already voted or not
		isvoted = false;
		for (uint i=0; i<question.voters.length; i++){
			if (question.voters[i].addr == sender){
				isvoted = true;
				break;
			}
		}
		
		// if shareholder haven't voted yet
		if (!isvoted){
			// add shareholder to the list of voters
			question.voters.push(Voter(sender));
			//check the answer, if answer 1 then add 1 to totalcountagree, otherwise totalcountdisagree
			if (answer == 1){
				question.totalcountagree = question.totalcountagree;
			}
			else{
				question.totalcountagree = question.totalcountdisagree;
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
			uint totalagree = questions[questionid].totalcountagree;
			uint totaldisagree = questions[questionid].totalcountdisagree;

			if (!questions[questionid].isopen){
				if (totalagree > totaldisagree){
					majorityanswer = 1;
				}
				else {
					majorityanswer = 0;
				}
			}	
    	}
		
	}
        
}