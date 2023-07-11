from fastapi import FastAPI
from database import Base, engine
from AppUser import router as app_router
from Profile import router as profile_router
from Family import router as family_router
from Post import router as post_router
from Comment import router as comment_router
from Tree import router as tree_router
from QuestType import router as quest_type_router
from Reward import router as reward_router
from Quest import router as quest_router
from Closeness import router as closeness_router
from Relation import router as relation_router
from TreeUser import router as tree_user_router
 
Base.metadata.create_all(engine) # Create the database
 
# Initialize app
app = FastAPI(title="こころい木")

# ===============================AppUser==============================================
app.include_router(app_router.router)

# # ===============================Profile============================================
app.include_router(profile_router.router)

# ===============================Family===============================================
app.include_router(family_router.router)

# ===============================Post=================================================
app.include_router(post_router.router)

# ===============================Comment==============================================
app.include_router(comment_router.router)

# ===============================Tree=================================================
app.include_router(tree_router.router)
 
# ===============================QuestType=============================================
app.include_router(quest_type_router.router)

# ===============================Reward=============================================
app.include_router(reward_router.router)
 
# ===============================Quest=============================================
app.include_router(quest_router.router)
    
# ===============================Closeness=============================================
app.include_router(closeness_router.router)

# ===============================Relation==============================================
app.include_router(relation_router.router)

# ===============================TreeUser==============================================
app.include_router(tree_user_router.router)