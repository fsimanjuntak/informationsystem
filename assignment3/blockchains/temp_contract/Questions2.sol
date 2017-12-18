pragma solidity^0.4.11;

contract Survey{

	address public director;
	
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
		mapping (address => Voter) voters;
	}
	
	uint questionCounter;
	mapping (uint => Question) public questions;
	mapping (addr => ShareHolder) public shareholders;
	
	//create shareholders
	function Survey(address[] shareholderNames) public {
		for (uint i = 0; i < shareholderNames.length; i++) {
            shareholders.push(ShareHolder({
                addr: shareholderNames[i],
                isallowedtovote: false
            }));
        }
	}	
	
	// create question
	function createQuestion(string questiondescription){
		questionID = questionCounter++;
		questions.push(Question(questionID,questiondescription,true,0,0,[]));
	}
	
	// enable shareholder to vote
	function enableVoterToAnswerQuestions(address voteraddress){
		if (voteraddress != director){
			shareholders[voteraddress].isallowedtovote = true;
		}
	}
	
	// disable shareholder to vote
	function disableVoterToAnswerQuestions(address voteraddress){
		if (voteraddress != director){
			shareholders[voteraddress].isallowedtovote = false;
		}	
	}
	
	function vote(uint questionid, uint answer) {
        Question storage question = questions[questionid];	
		require(question.isopen);
		
		#find if shareholder already voted or not
		isvoted = false;
		for (uint i=0; i<question.voters.length; i++){
			if (question.voters[i].addr == msg.sender){
				isvoted = true;
				break;
			}
		}
		
		if (isvoted){
		
		}
    }
	
	function closeVoting(uint questionid){
		require(question.isopen);
		questions[questionid].isopen = false;
	}
	
	function majorityDecision(uint questionid) constant returns (uint majorityanswer)
    {
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
		
		if (agree == notagree){
			majorityanswer = -9999;
		}
		else {
			if (agree > notagree){
				majorityanswer = 1;
			}
			else {
				majorityanswer = 0;
			}
		
		}
    }

}