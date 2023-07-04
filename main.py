from fastapi import FastAPI
from database import Base, engine
from AppUser import router as app_router
from Profile import router as profile_router
 
Base.metadata.create_all(engine) # Create the database
 
# Initialize app
app = FastAPI(title="こころい木")

# ===============================AppUser=============================================
app.include_router(app_router.router)

# # ===============================Profile=============================================
app.include_router(profile_router.router)

# # ===============================Family=============================================
# @app.get("/families", response_model = List[schemas.FamilySchema.Family], tags=["families 家族"])
# def 家族一覧取得(session: Session = Depends(get_session)):
 
#     family_list = session.query(models.FamilyModel.Family).all() # get all family items
 
#     return family_list 


# @app.get("/families/{id}", response_model=schemas.FamilySchema.Family, tags=["families 家族"])
# def 特定の家族の取得(id: int, session: Session = Depends(get_session)):
 
#     family = session.query(models.FamilyModel.Family).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not family:
#         raise HTTPException(status_code=404, detail=f"family item with id {id} not found")
 
#     return family
 
# @app.post("/families", response_model=schemas.FamilySchema.Family, status_code=status.HTTP_201_CREATED, tags=["families 家族"])
# def 家族の作成(family: schemas.FamilySchema.FamilyCreate, session: Session = Depends(get_session)):
 
#     familydb = models.FamilyModel.Family(
#         name=family.name,
#         createdAt=datetime.today(),
#         updatedAt=datetime.today()
#     )
 
#     session.add(familydb)
#     session.commit()
#     session.refresh(familydb)
 
#     return familydb
 
 
# @app.put("/families/{id}", response_model=schemas.FamilySchema.Family, tags=["families 家族"])
# def 特定の家族の更新(id: int, family: schemas.FamilySchema.FamilyCreate, session: Session = Depends(get_session)):
#     # Check if the family item with the given id exists
#     existing_family = session.query(models.FamilyModel.Family).get(id)
#     if not existing_family:
#         raise HTTPException(status_code=404, detail=f"family item with id {id} not found")

#     # Update the attributes of the existing_family with the values from the family parameter
#     existing_family.name=family.name

#     session.commit()
#     session.refresh(existing_family)

#     return existing_family
 
# @app.delete("/families/{id}", tags=["families 家族"])
# def 特定の家族の削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     family = session.query(models.FamilyModel.Family).get(id)
 
#     # if family item with given id exists, delete it from the database. Otherwise raise 404 error
#     if family:
#         session.delete(family)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"family item with id {id} not found")
 
#     return None

# # ===============================Post=============================================
# @app.get("/posts", response_model = List[schemas.PostSchema.Post], tags=["posts"])
# def 投稿一覧取得(session: Session = Depends(get_session)):
 
#     post_list = session.query(models.PostModel.Post).all() # get all post items
 
#     return post_list 


# @app.get("/posts/{id}", response_model=schemas.PostSchema.Post, tags=["posts"])
# def 特定の投稿の取得(id: int, session: Session = Depends(get_session)):
 
#     post = session.query(models.PostModel.Post).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not post:
#         raise HTTPException(status_code=404, detail=f"post item with id {id} not found")
 
#     return post
 
# @app.post("/posts", response_model=schemas.PostSchema.Post, status_code=status.HTTP_201_CREATED, tags=["posts"])
# def 投稿の作成(post: schemas.PostSchema.PostCreate, session: Session = Depends(get_session)):
 
#     postdb = models.PostModel.Post(
#         user_id=post.user_id,
#         kids=post.kids,
#         content=post.content,
#         image_url=post.image_url,
#         like=post.like,
#         createdAt=datetime.today(),
#         updatedAt=datetime.today(),
#         publishedAt=datetime.today()
#     )
 
#     session.add(postdb)
#     session.commit()
#     session.refresh(postdb)
 
#     return postdb
 
 
# @app.put("/posts/{id}", response_model=schemas.PostSchema.Post, tags=["posts"])
# def 特定の投稿の更新(id: int, post: schemas.PostSchema.PostCreate, session: Session = Depends(get_session)):
#     # Check if the post item with the given id exists
#     existing_post = session.query(models.PostModel.Post).get(id)
#     if not existing_post:
#         raise HTTPException(status_code=404, detail=f"Post item with id {id} not found")

#     # Update the attributes of the existing_post with the values from the post parameter
#     existing_post.user_id = post.user_id
#     existing_post.kids = post.kids
#     existing_post.content = post.content
#     existing_post.image_url = post.image_url
#     existing_post.like = post.like

#     session.commit()
#     session.refresh(existing_post)

#     return existing_post
 
# @app.delete("/posts/{id}", tags=["posts"])
# def 特定の投稿の削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     post = session.query(models.PostModel.Post).get(id)
 
#     # if post item with given id exists, delete it from the database. Otherwise raise 404 error
#     if post:
#         session.delete(post)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"post item with id {id} not found")
 
#     return None


# # ===============================Comment=============================================
# @app.get("/comments", response_model = List[schemas.CommentSchema.Comment], tags=["comments"])
# def コメント一覧取得(session: Session = Depends(get_session)):
 
#     comment_list = session.query(models.CommentModel.Comment).all() # get all Comment items
 
#     return comment_list 


# @app.get("/comments/{id}", response_model=schemas.CommentSchema.Comment, tags=["comments"])
# def 特定のコメントの取得(id: int, session: Session = Depends(get_session)):
 
#     comment = session.query(models.CommentModel.Comment).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not comment:
#         raise HTTPException(status_code=404, detail=f"comment item with id {id} not found")
 
#     return comment
 
# @app.post("/comments", response_model=schemas.CommentSchema.Comment, status_code=status.HTTP_201_CREATED, tags=["comments"])
# def コメントの作成(comment: schemas.CommentSchema.CommentCreate, session: Session = Depends(get_session)):
 
#     commentdb = models.CommentModel.Comment(
#         parent_id = comment.parent_id,
#         post_id = comment.post_id,
#         user_id = comment.user_id,
#         content = comment.content,
#         createdAt= datetime.today()
#     )
 
#     session.add(commentdb)
#     session.commit()
#     session.refresh(commentdb)
 
#     return commentdb
 
 
# @app.put("/comments/{id}", response_model=schemas.CommentSchema.Comment, tags=["comments"])
# def 特定のコメントの更新(id: int, comment: schemas.CommentSchema.CommentCreate, session: Session = Depends(get_session)):
#     # Check if the comment item with the given id exists
#     existing_comment = session.query(models.CommentModel.Comment).get(id)
#     if not existing_comment:
#         raise HTTPException(status_code=404, detail=f"Comment item with id {id} not found")

#     # Update the attributes of the existing_comment with the values from the comment parameter
#     existing_comment.parent_id = comment.parent_id
#     existing_comment.post_id = comment.post_id
#     existing_comment.user_id = comment.user_id
#     existing_comment.content = comment.content

#     session.commit()
#     session.refresh(existing_comment)

#     return existing_comment
 
# @app.delete("/comments/{id}", tags=["comments"])
# def 特定のコメントの削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     comment = session.query(models.CommentModel.Comment).get(id)
 
#     # if comment item with given id exists, delete it from the database. Otherwise raise 404 error
#     if comment:
#         session.delete(comment)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"comment item with id {id} not found")
 
#     return None

 
# # ===============================Tree=============================================
# @app.get("/trees", response_model = List[schemas.TreeSchema.Tree], tags=["trees"])
# def 木一覧取得(session: Session = Depends(get_session)):
 
#     tree_list = session.query(models.TreeModel.Tree).all() # get all Tree items
 
#     return tree_list 


# @app.get("/trees/{id}", response_model=schemas.TreeSchema.Tree, tags=["trees"])
# def 特定の木の取得(id: int, session: Session = Depends(get_session)):
 
#     tree = session.query(models.TreeModel.Tree).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not tree:
#         raise HTTPException(status_code=404, detail=f"tree item with id {id} not found")
 
#     return tree
 
# @app.post("/trees", response_model=schemas.TreeSchema.Tree, status_code=status.HTTP_201_CREATED, tags=["trees"])
# def 木の作成(tree: schemas.TreeSchema.TreeCreate, session: Session = Depends(get_session)):
 
#     treedb = models.TreeModel.Tree(
#         growth_stage = tree.growth_stage,
#         quest = tree.quest,
#         watering = datetime.today()
#     )
 
#     session.add(treedb)
#     session.commit()
#     session.refresh(treedb)
 
#     return treedb
 
 
# @app.put("/trees/{id}", response_model=schemas.TreeSchema.Tree, tags=["trees"])
# def 特定の木の更新(id: int, tree: schemas.TreeSchema.TreeCreate, session: Session = Depends(get_session)):
#     # Check if the tree item with the given id exists
#     existing_tree = session.query(models.TreeModel.Tree).get(id)
#     if not existing_tree:
#         raise HTTPException(status_code=404, detail=f"Tree item with id {id} not found")

#     # Update the attributes of the existing_tree with the values from the tree parameter
#     existing_tree.growth_stage = tree.growth_stage
#     existing_tree.quest = tree.quest

#     session.commit()
#     session.refresh(existing_tree)

#     return existing_tree
 
# @app.delete("/trees/{id}", tags=["trees"])
# def 特定の木の削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     tree = session.query(models.TreeModel.Tree).get(id)
 
#     # if tree item with given id exists, delete it from the database. Otherwise raise 404 error
#     if tree:
#         session.delete(tree)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"tree item with id {id} not found")
 
#     return None

 
# # ===============================QuestType=============================================
# @app.get("/quest_types", response_model = List[schemas.QuestTypeSchema.QuestType], tags=["quest_types"])
# def クエストタイプ一覧取得(session: Session = Depends(get_session)):
 
#     questtype_list = session.query(models.QuestTypeModel.QuestType).all() # get all QuestType items
 
#     return questtype_list 


# @app.get("/quest_types/{id}", response_model=schemas.QuestTypeSchema.QuestType, tags=["quest_types"])
# def 特定のクエストタイプの取得(id: int, session: Session = Depends(get_session)):
 
#     questtype = session.query(models.QuestTypeModel.QuestType).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not questtype:
#         raise HTTPException(status_code=404, detail=f"questtype item with id {id} not found")
 
#     return questtype
 
# @app.post("/quest_types", response_model=schemas.QuestTypeSchema.QuestType, status_code=status.HTTP_201_CREATED, tags=["quest_types"])
# def クエストタイプの作成(questtype: schemas.QuestTypeSchema.QuestTypeCreate, session: Session = Depends(get_session)):
 
#     questtypedb = models.QuestTypeModel.QuestType(
#         kinds = questtype.kinds,
#         online = questtype.online
#     )

#     session.add(questtypedb)
#     session.commit()
#     session.refresh(questtypedb)
 
#     return questtypedb
 
 
# @app.put("/quest_types/{id}", response_model=schemas.QuestTypeSchema.QuestType, tags=["quest_types"])
# def 特定のクエストタイプの更新(id: int, questtype: schemas.QuestTypeSchema.QuestTypeCreate, session: Session = Depends(get_session)):
#     # Check if the questtype item with the given id exists
#     existing_tree = session.query(models.QuestTypeModel.QuestType).get(id)
#     if not existing_tree:
#         raise HTTPException(status_code=404, detail=f"QuestType item with id {id} not found")

#     # Update the attributes of the existing_tree with the values from the questtype parameter
#     existing_tree.kinds = questtype.kinds
#     existing_tree.online = questtype.online

#     session.commit()
#     session.refresh(existing_tree)

#     return existing_tree
 
# @app.delete("/quest_types/{id}", tags=["quest_types"])
# def 特定のクエストタイプの削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     questtype = session.query(models.QuestTypeModel.QuestType).get(id)
 
#     # if questtype item with given id exists, delete it from the database. Otherwise raise 404 error
#     if questtype:
#         session.delete(questtype)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"questtype item with id {id} not found")
 
#     return None

 
# # ===============================Reward=============================================
# @app.get("/rewards", response_model = List[schemas.RewardSchema.Reward], tags=["rewards"])
# def 褒美一覧取得(session: Session = Depends(get_session)):
 
#     reward_list = session.query(models.RewardModel.Reward).all() # get all Reward items
 
#     return reward_list 


# @app.get("/rewards/{id}", response_model=schemas.RewardSchema.Reward, tags=["rewards"])
# def 特定の褒美の取得(id: int, session: Session = Depends(get_session)):
 
#     reward = session.query(models.RewardModel.Reward).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not reward:
#         raise HTTPException(status_code=404, detail=f"reward item with id {id} not found")
 
#     return reward
 
# @app.post("/rewards", response_model=schemas.RewardSchema.Reward, status_code=status.HTTP_201_CREATED, tags=["rewards"])
# def 褒美の作成(reward: schemas.RewardSchema.RewardCreate, session: Session = Depends(get_session)):
 
#     rewarddb = models.RewardModel.Reward(
#         content = reward.content
#     )

#     session.add(rewarddb)
#     session.commit()
#     session.refresh(rewarddb)
 
#     return rewarddb
 
 
# @app.put("/rewards/{id}", response_model=schemas.RewardSchema.Reward, tags=["rewards"])
# def 特定の褒美の更新(id: int, reward: schemas.RewardSchema.RewardCreate, session: Session = Depends(get_session)):
#     # Check if the reward item with the given id exists
#     existing_reward = session.query(models.RewardModel.Reward).get(id)
#     if not existing_reward:
#         raise HTTPException(status_code=404, detail=f"Reward item with id {id} not found")

#     # Update the attributes of the existing_reward with the values from the reward parameter
#     existing_reward.content = reward.content

#     session.commit()
#     session.refresh(existing_reward)

#     return existing_reward
 
# @app.delete("/rewards/{id}", tags=["rewards"])
# def 特定の褒美の削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     reward = session.query(models.RewardModel.Reward).get(id)
 
#     # if reward item with given id exists, delete it from the database. Otherwise raise 404 error
#     if reward:
#         session.delete(reward)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"reward item with id {id} not found")
 
#     return None

 
# # ===============================Quest=============================================
# @app.get("/quests", response_model = List[schemas.QuestSchema.Quest], tags=["quests"])
# def クエスト一覧取得(session: Session = Depends(get_session)):
 
#     quests_list = session.query(models.QuestModel.Quest).all() # get all quests items
 
#     return quests_list 


# @app.get("/quests/{id}", response_model=schemas.QuestSchema.Quest, tags=["quests"])
# def 特定のクエストの取得(id: int, session: Session = Depends(get_session)):
 
#     quests = session.query(models.QuestModel.Quest).get(id) # get item with the given id
 
#     # check if id exists. If not, return 404 not found response
#     if not quests:
#         raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")
 
#     return quests
 
# @app.post("/quests", response_model=schemas.QuestSchema.Quest, status_code=status.HTTP_201_CREATED, tags=["quests"])
# def クエストの作成(quests: schemas.QuestSchema.QuestCreate, session: Session = Depends(get_session)):
 
#     questsdb = models.QuestModel.Quest(
#         content=quests.content,
#         quest_kinds=quests.quest_kinds,
#         completed=quests.completed
#     )
 
#     session.add(questsdb)
#     session.commit()
#     session.refresh(questsdb)
 
#     return questsdb
 
 
# @app.put("/quests/{id}", response_model=schemas.QuestSchema.Quest, tags=["quests"])
# def 特定のクエストの更新(id: int, quests: schemas.QuestSchema.QuestCreate, session: Session = Depends(get_session)):
#     # Check if the quests item with the given id exists
#     existing_quests = session.query(models.QuestModel.Quest).get(id)
#     if not existing_quests:
#         raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")

#     # Update the attributes of the existing_quests with the values from the quests parameter
#     existing_quests.content=quests.content
#     existing_quests.quest_kinds=quests.quest_kinds
#     existing_quests.completed=quests.completed

#     session.commit()
#     session.refresh(existing_quests)

#     return existing_quests
 
# @app.delete("/quests/{id}", tags=["quests"])
# def 特定のクエストの削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     quests = session.query(models.QuestModel.Quest).get(id)
 
#     # if quests item with given id exists, delete it from the database. Otherwise raise 404 error
#     if quests:
#         session.delete(quests)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")
 
#     return None
 
# # ===============================Closeness=============================================
# @app.get("/closeness", response_model = List[schemas.ClosenessSchema.Closeness], tags=["closeness"])
# def Closenessの一覧取得(session: Session = Depends(get_session)):
 
#     closeness_list = (session.query(models.ClosenessModel.Closeness).all()) # get all closeness items
 
#     return closeness_list 


# @app.get("/closeness/{id}", response_model=schemas.ClosenessSchema.Closeness, tags=["closeness"])
# def 特定のClosenessを取得(id: int, session: Session = Depends(get_session)):
#     close = session.query(models.ClosenessModel.Closeness).get(id) # get item with the given id

#     # Check if close exists
#     if not close:
#         raise HTTPException(status_code=404, detail=f"Closeness with id {id} not found")

#     return close
 
# @app.post("/closeness", response_model=schemas.ClosenessSchema.Closeness, status_code=status.HTTP_201_CREATED, tags=["closeness"])
# def Closenessの作成(closeness: schemas.ClosenessSchema.ClosenessCreate, session: Session = Depends(get_session)):

#     closenessdb = models.ClosenessModel.Closeness(
#         tree_id=closeness.tree_id,
#         close_meter=closeness.close_meter,
#     )
 
#     session.add(closenessdb)
#     session.commit()
#     session.refresh(closenessdb)

#     return closenessdb
 
 
# @app.put("/closeness/{id}", response_model=schemas.ClosenessSchema.Closeness, tags=["closeness"])
# def 特定のClosenessの更新(id: int, closeness: schemas.ClosenessSchema.ClosenessCreate, session: Session = Depends(get_session)):
#     # Check if the closeness item with the given id exists
#     existing_closeness = session.query(models.ClosenessModel.Closeness).get(id)
#     if not existing_closeness:
#         raise HTTPException(status_code=404, detail=f"Closeness item with id {id} not found")

#     # Update the attributes of the existing_closeness with the values from the closeness parameter
#     existing_closeness.tree_id = closeness.tree_id
#     existing_closeness.close_meter = closeness.close_meter

#     session.commit()
#     session.refresh(existing_closeness)

#     return existing_closeness
 
# @app.delete("/closeness/{id}", tags=["closeness"])
# def 特定のClosenessの削除(id: int, session: Session = Depends(get_session)):
 
#     # get the given id
#     closeness = session.query(models.ClosenessModel.Closeness).get(id)
 
#     # if closeness item with given id exists, delete it from the database. Otherwise raise 404 error
#     if closeness:
#         session.delete(closeness)
#         session.commit()
#     else:
#         raise HTTPException(status_code=404, detail=f"closeness item with id {id} not found")
 
#     return None