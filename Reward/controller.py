from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
import models, schemas

#get all reward
def get_reward(session: Session):
    reward_list = session.query(models.RewardModel.Reward).all() # get all Reward items
    return reward_list 

#get reward by id
def get_reward_by_id(session: Session, id: int):
    reward = session.query(models.RewardModel.Reward).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not reward:
        raise HTTPException(status_code=404, detail=f"reward item with id {id} not found")
 
    return reward

#create reward
def create_reward(session: Session, reward: schemas.RewardSchema.RewardCreate):
    rewarddb = models.RewardModel.Reward(
        content = reward.content
    )

    session.add(rewarddb)
    session.commit()
    session.refresh(rewarddb)
 
    return rewarddb

#update reward by id
def update_reward(session: Session, reward: schemas.RewardSchema.RewardCreate, id: int):
    # Check if the reward item with the given id exists
    existing_reward = session.query(models.RewardModel.Reward).get(id)
    if not existing_reward:
        raise HTTPException(status_code=404, detail=f"Reward item with id {id} not found")

    # Update the attributes of the existing_reward with the values from the reward parameter
    existing_reward.content = reward.content

    session.commit()
    session.refresh(existing_reward)

    return existing_reward
 
#delete reward by id
def delete_reward(session: Session, id: int):
    # get the given id
    reward = session.query(models.RewardModel.Reward).get(id)
 
    # if reward item with given id exists, delete it from the database. Otherwise raise 404 error
    if reward:
        session.delete(reward)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"reward item with id {id} not found")

    return {"message": f"reward item with id {id} is deleted successful"}