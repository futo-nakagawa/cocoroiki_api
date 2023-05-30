import json
import pathlib
from typing import List, Union
from fastapi import FastAPI, Response
from models import Track

app = FastAPI()
data = []
@app.on_event("startup")
async def startup_event():
    datapath = pathlib.Path() / "data" / "tracks.json"
    with open(datapath, "r") as f:
        tracks = json.load(f)
        for track in tracks:
            data.append(Track(**track).dict())

# GET all the tracks
@app.get("/tracks/", response_model=List[Track])
def track():
    return data

# GET by id
@app.get("/tracks/{track_id}", response_model=Union[Track, str])
def track(track_id: int, response: Response):
    #find the track with the given ID, or None if it does not exist
    track = None
    for t in data:
        if t["id"] == track_id:
            track = t
            break

    if track is None:
        response.status_code = 404
        return "Not found"
    return track

#POST
@app.post("/tracks/", response_model=Track, status_code=201)
def create_track(track: Track):
    track_dict = track.dict()
    track_dict["id"] = max(data, key=lambda x:x ["id"]).get("id") + 1
    data.append(track_dict)
    return track_dict

#PUT
@app.put("/tracks/{track_id}", response_model=Union[Track, str])
def track(track_id: int, updated_track: Track, response: Response):
    #find the track with the given ID, or None if it does not exist
    track = None
    for t in data:
        if t["id"] == track_id:
            track = t
            break

    if track is None:
        response.status_code = 404
        return "Not found"
    
    for key, val in updated_track.dict().items():
        if key != "id":
            track[key] = val
    return track

#DELETE by id
@app.delete("/tracks/{track_id}/")
def track(track_id: int, response: Response):
    track_index = None
    # get the index of the track to delete
    for idx ,t in enumerate(data):
        if t["id"] == track_id:
            track_index = idx
            break

    if track_index is None:
        # if a track with given ID doesn't exist, set 404 code and return string
        response.status_code = 404
        return "Not found"
    
    # delete the track from the data, and return empty 200 response
    del data[track_index]
    return Response(status_code=200)