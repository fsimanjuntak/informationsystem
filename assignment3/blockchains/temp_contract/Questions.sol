pragma solidity^0.4.11;

contract Survey{

	address public director;
	
	struct ShareHolder {
		address addr;
		bool voted;
		uint answer;
	}
	
	struct Question {
		uint id;
		string description;
		boolean isopen;
		mapping (address => ShareHolder) voters;
	}
	
	uint questionCounter;
	mapping (uint => Question) public questions;
	
	function createQuestion(string questiondescription){
		questionID = questionCounter++;
		questions.push(Question(questionID,questiondescription,true,[]));
	}
	
	function addVoterIntoQuestion(address voteraddress, uint questionid){
		if (voteraddress != director){
			questions[questionid].voters.push(ShareHolder(voteraddress,false,0));
		}
	}
	
	function removeVoterFromQuestion(address voteraddress, uint questionid){
		bool found = false;
		uint tempidx = 0; 
		for (uint i=0; i< questions[questionid].voters.length; i++){
			if (questions[questionid].voters[j].addr == voteraddress){
				found = true;
				tempidx = i;
				break;
			}
		}
		
		if(found){
			questions[questionid].voters[tempidx].pop();
		}		
	}
	
	function vote(uint questionid, uint answer) {
        Question storage question = questions[questionid];	
		require(question.isopen);
		for (uint i=0; i<question.voters.length; i++){
			if (question.voters[i].addr == msg.sender && !question.voters[i].voted){
				questions[questionid].voters[i].answer = answer;
				questions[questionid].voters[i].voted = true;
				break;
			}
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