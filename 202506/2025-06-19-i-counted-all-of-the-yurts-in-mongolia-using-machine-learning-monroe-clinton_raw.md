Title: I Counted All of the Yurts in Mongolia Using Machine Learning

URL Source: https://monroeclinton.com/counting-all-yurts-in-mongolia/

Markdown Content:
The _Fall of Civilizations_ podcast put out a [6¾-hour episode](https://www.youtube.com/watch?v=YyqS9V7yHQA) on the history of the Mongol Empire, which I eagerly listened to. After finishing the episode I wondered about contemporary Mongolian society, I wanted to learn what the lands that the Mongol Empire exploded from are like in our current day. There are many ways to try to understand a society, whether it be quantifying it or looking at the lived experiences within it. If you look at data provided by the World Bank, you’ll see a country that has rapidly reduced poverty in the 21st century, has a high economic growth rate, a healthy fertility rate, and is solidly an upper-middle-income country. While Mongolia is a republic with a competitive party system, [Worldwide Governance Indicators](https://www.worldbank.org/en/publication/worldwide-governance-indicators/interactive-data-access) from the World Bank show a government that has issues with corruption, regulatory quality, and effectiveness.

| Indicator | Value | Years |
| --- | --- | --- |
| Population | 3,481,145 | 2023 |
| Fertility rate | 2.7 | 2023 |
| Intentional homicides (per 100,000 people) | 6 | 2021 |
| Individuals using the Internet (% of population) | 1% → 83% | 2000 → 2023 |
| Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population) | 11.6% → 0.2% | 2002 → 2022 |
| Average GDP growth | 6.62% | 2003 → 2023 |
| GDP per capita, PPP (current international $) | $4,399.4 → $18,004.9 | 2003 → 2023 |

> (“Mongolia”)

All of these indicators are interesting to look at, but they don’t really show what a society is like. I feel you get much more understanding by going to a country, walking the streets, and talking to people there. If you’re unable to do this, the next best thing is spending hours exploring Google Maps, which I did. I opened a satellite view of Ulaanbaatar, the capital of Mongolia. I saw new glass buildings, Soviet-designed apartment blocks (called ugsarmal), impressive government buildings, factories, and industrial areas. But something stood out to me. Yurts, extending for kilometers in all directions.

![Image 1: Satellite view of Ulaanbaatar containing yurts](https://monroeclinton.com/counting-all-yurts-in-mongolia/yurts-1.jpg)

> Maps Data: Google © 2025 Airbus, CNES / Airbus, Maxar Technologies

Naturally, I was impressed by the quantity of yurts I saw, and I was curious: just how many yurts (ger in Mongolian) are in Mongolia and why? This set me on the path drawing bounding boxes on over 10,000 yurts to train a machine learning model to count the rest of the yurts in the country. While I was training the model, I wondered what the story behind these yurts are, I did a small investigation for later in this article. For now, this is the story of counting them.

Counting all the yurts in Mongolia
----------------------------------

I was unable to find a count of the yurts in Mongolia, this left me with the task of doing it myself. Although I had never studied or worked with machine learning, I knew through some osmosis that machine learning is well fit for this task. I created a simple plan in my brain:

1.   Train a model to identify yurts
2.   Reduce input space and parallelize searching of input space
3.   Keep track of the yurts found

### Training a model to identify yurts

The first thing I needed was training data, and lots of it. There’s many different options for satellite imagery such as [Mapbox](https://www.mapbox.com/imagery), [Google Maps](https://developers.google.com/maps/documentation/tile), and [ArcGIS](https://developers.arcgis.com/rest/basemap-styles/arcgis-imagery-webmap-get/). I decided to use Google Maps since I’m already familiar with it.

For digital maps, many systems break the world up into a series of 256 x 256 tiles identified by X, Y, Z values. This is referred to as tiled web maps and allows for progressively loading maps at different zoom levels and positions. The zoom level values tend to be 0 through 20, where 0 has the least tiles and 20 the most. The formula for calculating the number of tiles at a given zoom (z) level is: 2 z∗2 z 2^z * 2^z . This means increasing `z` by one will increase the tile count by four times.

I wrote a Python script that generated tiles from a box around Ulaanbaatar and downloaded them to a folder to use as training data. To list the tiles inside a bounding box made up of a southwest and northeast coordinates, I used the [mercantile package](https://mercantile.readthedocs.io/en/latest/).

```
for tile in mercantile.tiles(sw_lng, sw_lat, ne_lng, ne_lat, zooms=z):
    download_tile(*tile)
```

![Image 2: Sample tile from Google Maps](https://monroeclinton.com/counting-all-yurts-in-mongolia/tile-1.jpeg)![Image 3: Sample tile from Google Maps](https://monroeclinton.com/counting-all-yurts-in-mongolia/tile-2.jpeg)![Image 4: Sample tile from Google Maps](https://monroeclinton.com/counting-all-yurts-in-mongolia/tile-3.jpeg)

> Tiles from Google Maps, you can see yurts on the right tile. Maps Data: Google © 2025 Airbus, CNES / Airbus, Maxar Technologies

I decided to start at zoom level `17` as it is the lowest zoom level that I can still identify yurts at. Once I downloaded several hundred tiles at this zoom level, I needed a way to label the yurts on these tiles. Labeling is the process of drawing boxes around objects in an image. The idea is to draw these boxes manually, creating what is called annotated data, and then training a model to do the labeling using the annotated data. There’s an open source tool called [Label Studio](https://labelstud.io/) that does just this.

![Image 5: Label Studio showing yurts labeled](https://monroeclinton.com/counting-all-yurts-in-mongolia/label-studio.jpg)

> Here I drew bounding boxes on the tile around the yurts.

A couple dozen yurts later and I wanted to try and train a model based on my tiny amount of annotated data. I had the choice between object detection (bounding boxes) and segmentation (outline objects). Segmentation probably would be more accurate because yurts are not rectangular, but it seemed like it would take longer to setup. I decided to go with object detection.

I looked at various ways to train an object detection model, my requirements were:

*   Open source
*   As simple as possible to setup
*   Able to quickly iterate
*   Detection speed of the model is a priority due to the potentially large amount of data
*   Has good default settings around data augmentation, warmups, loss functions, etc
*   Monitor current and previous training runs to compare accuracy

After doing a brief survey of the machine learning landscape, I landed on using [YOLO11](https://docs.ultralytics.com/) by Ultralytics. The YOLO series is a set of models that can complete computer vision tasks, and can be trained with custom data. In Label Studio you’re able to export to many different dataset types, YOLO being one of them. After exporting my annotated data as a YOLO dataset, I split the dataset into training and validation data and configured the dataset in `dataset.yaml` for YOLO to use.

```
train: images/train
val: images/val

nc: 1
names:
  - yurt
```

From the ultralytics package, I used the YOLO class to use their pre-trained `yolo11n` object detection model. Ultralytics allows easy tuning of the model with annotated data through the `train` method of the `YOLO` class. The tuned model can be exported through `export` in various formats.

```
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
model.train(
    data="dataset.yaml",
    device="cpu",
)

path = model.export(name="yurt")
```

With some testing I found my Yurt model was less than adequate, which I expected due to the tiny amount of annotated data. I then did a couple hours of labeling, but the model would always miss around 10-15% of the yurts in a given tile. At this point I had two options, either increase the zoom level or gather more training data. To base my decision I decided to calculate how many tiles I would need to search at each zoom level.

### Refining the search area

Mongolia is 1,564,116 square kilometers, using this we can calculate how many tiles at each zoom level there are in Mongolia. The world has 2 z∗2 z 2^z * 2^z tiles, so on a single axis there are 2 z 2^z tiles. The map projection is from a sphere a tile will represent more or less area depending on the latitude. To find the width of the projection at a latitude for Web Mercator, we can use this formula where R=6,378.137 R = 6,378.137 is the radius of the equator in kilometers and ϕ=47.923107575288114\phi = 47.923107575288114 is the latitude of Mongolia in degrees which is converted to radians:

2 π∗R∗cos⁡(ϕ∗π 180)=26,855.3636571 2\pi * R * \cos(\phi * \dfrac{\pi}{180}) = 26,855.3636571

We then need to divide the number of tiles on the x-axis at this location to get the width of a tile. For the area of a tile, just square the width and divide the area of Mongolia by the area of a single tile to get the tile count.

| Zoom Level | Tile Count |
| --- | --- |
| 17 | 37,258,617 |
| 18 | 149,034,469 |
| 19 | 596,137,879 |
| 20 | 2,384,551,518 |

Since Mongolia is such a large country, I began to wonder if there are more ways to reduce the amount of tiles other than just zoom level. It’s a sparsely populated country, with much of the country being uninhabited. Also, nearly all yurts are located in urban areas, with the City of Ulaanbaatar estimating 60% of the population lives in ger (yurt) districts (City of Ulaanbaatar 17).

I used [overpass turbo](https://overpass-turbo.eu/) to do a query for all the places human settlements might be in the country and exported this data as GeoJSON. The query returned several thousand points of interest.

```
[out:json][timeout:25];
{{geocodeArea:Mongolia}}->.searchArea;
(
  node[place](area.searchArea);
  node[man_made](area.searchArea);
  node[historic](area.searchArea);
);
out body;
>;
out skel qt;
```

I wanted to know how many unique tiles for searching a 2,000 meter area around each point there are, so I wrote a script to do this using geopandas.

```
gdf = gpd.read_file("./mongolia.geojson")
gdf_merc = gdf.to_crs("EPSG:3857")
gdf_merc["buffer"] = gdf_merc.geometry.buffer(2000)

gdf_buffer = gdf_merc.set_geometry("buffer").to_crs("EPSG:4326")

tiles = {}
for polygon in gdf_buffer.geometry:
    minx, miny, maxx, maxy = polygon.bounds

    for tile in mercantile.tiles(minx, miny, maxx, maxy, zooms=Z):
        tiles["{}-{}-{}".format(str(tile.x), str(tile.y), str(tile.z))] = True
```

| Zoom Level | Tile Count |
| --- | --- |
| 17 | 270,559 |
| 18 | 1,016,617 |
| 19 | 3,938,174 |
| 20 | 15,506,872 |

### Building a model backend for labeling

To speed up the labeling of yurts I wanted Label Studio to use my model to label yurts. Label Studio has the ability to integrate with a model backend, essentially an API wrapper around a model, to request predictions. When labeling a tile, Label Studio makes a request to this API for predictions. The API returns the bounding boxes for the tile. I fix any mistakes the model made, and submit the tile. Every so often I retrain the model, creating a feedback loop that improves the model with more and more annotated data.

```
class YurtModel:
    # Initialize trained model to reuse across requests
    def __init__(self):
        self.model = YOLO("best.pt", task="detect")

    # Task a task sent by Label Studio, and return bounding boxes of yurts
    def predict(self, tasks):
        predictions = []
        for task in tasks:
            # Get the path to the file from label studio
            path = get_local_path(
                task["data"]["image"],
                task_id=task["id"],
            )

            results = self.model(path)

            for result in results:
                regions = []
                for prediction in result.boxes:
                    xyxy = prediction.xyxy[0].tolist()
                    regions.append({
                        "model_version": "1.0",
                        "from_name": "label",
                        "to_name": "image",
                        "type": "rectanglelabels",
                        "score": prediction.conf.item(),
                        "value": {
                            "x": xyxy[0] / 256 * 100,
                            "y": xyxy[1] / 256 * 100,
                            "width": (xyxy[2] - xyxy[0]) / 256 * 100,
                            "height": (xyxy[3] - xyxy[1]) / 256 * 100,
                            "rectanglelabels": [
                                "yurt",
                            ],
                        },
                    })

                all_scores = [region["score"] for region in regions if "score" in region]
                avg_score = sum(all_scores) / max(len(all_scores), 1)

                predictions.append({
                    "result": regions,
                    "score": avg_score,
                    "model_version": "1.0",
                })

        return {
            "results": predictions,
        }

model = YurtModel()
```

We then need to fill out the API routes that Label Studio expects, which is a `/predict` route for label studio to send tiles and receive predictions, a `/setup` route to do any initialization required, and a `/health` route to do health checks on. I used [FastAPI](https://fastapi.tiangolo.com/) to build the API and use the `YurtModel` from above.

```
@app.post("/predict")
async def predict(request: Request):
    res = await request.json()
    return model.predict(res["tasks"])

@app.post("/setup")
async def setup():
    return {
        "model_version": "1.0",
    }

@app.get("/health")
async def health():
    return {
        "status": "UP",
        "model_class": str(YurtModel.__class__),
    }
```

By relying on the model to find most of the yurts when labeling, I was able to rapidly create more annotated data. I quickly built a dataset of over 10,000 yurts.

### Monitoring accuracy of each model

### Scaling training of models

As the size of the annotated data grew, training the models on my laptop became too slow. I decided to use [vast.ai](https://vast.ai/) to rent GPUs to do my training runs. To train the models on vast.ai, I needed everything to run in Docker. I wrote a Dockerfile for the training script, and I pushed it to [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry). In vast.ai I set up authentication with the private image registry so it could pull the image I pushed up.

![Image 6: vast.ai Docker authentication](https://monroeclinton.com/counting-all-yurts-in-mongolia/docker-auth.png)

> Docker authentication in vast.ai

Here is the Dockerfile that I used to run the training script on the dataset I created.

```
FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /app

# Copy training script, annotated data, and requirements to image
COPY scripts/train_model.py .
COPY datasets ./datasets
COPY dataset.yaml .
COPY pyproject.toml .
COPY uv.lock .

# Needed for ...
RUN apt-get update -y && apt-get install -y libgl1-mesa-dev libglib2.0-0

# Install package requirements
RUN uv sync --no-dev

# Run the training script
CMD ["uv", "run", "python", "train_model.py"]
```

In order to build and push this image to GitHub I ran:

```
docker build -t ghcr.io/monroeclinton/yurt -f Dockerfile .
docker push ghcr.io/monroeclinton/yurt:latest
```

Since the training happened in ephemeral containers, I needed a way to retrieve the finished model. I decided to upload the model to S3 after it finished training. To monitor the accuracy of the models, I also needed the metadata associated with the runs, so I uploaded everything in the run folder to S3.

```
model = YOLO("yolo11n.pt")

model.train(
    data="dataset.yaml",
    epochs=1000,
    patience=150,
    imgsz=256,
    device="cuda",
)

path = model.export(name="yurt")
train_dir = os.path.dirname(os.path.dirname(path))

s3 = boto3.client(
    service_name ="s3",
    endpoint_url=os.environ["S3_ENDPOINT"],
    aws_access_key_id=os.environ["S3_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["S3_SECRET_ACCESS_KEY"],
    region_name=os.environ["S3_REGION"],
)

timestamp = time.time()

for root, dirs, files in os.walk(train_dir):
    for file in files:
        local_path = os.path.join(root, file)
        s3_key = f"models/{int(timestamp)}/{os.path.relpath(local_path, train_dir)}"
        s3.upload_file(local_path, os.environ["S3_BUCKET"], s3_key)
```

### Deploying models and searching Mongolia

After dozens of training runs and greatly improving the accuracy of the model, I decided to finally do my count of Mongolia. There were many options to run my deployment, however I made my choice based on three criteria:

*   Simplicity in setup and deployment
*   At least 100 instances of my model should be run
*   The bottleneck is I/O (downloading tiles), so should be deployed on many CPUs

Based on these criteria, I used [Docker Swarm](https://docs.docker.com/engine/swarm/) to orchestrate the workload. It’s already packaged in Docker, so there’s no need to install anything else. Docker Swarm also is fairly simple to set up, scale, and deploy services with. I rented eight servers, each with 16 vCPUs (128 vCPUs total), and connected them over a private network.

I picked one server to be the [manager node](https://docs.docker.com/engine/swarm/how-swarm-mode-works/nodes/#manager-nodes). On this server, I ran this to initialize the swarm:

```
docker swarm init --advertise-addr 10.0.0.2
```

This command sets up the swarm and prints a command to run on the worker nodes to connect them to the manager. Each worker node joined using the token and the manager’s address:

```
docker swarm join --token SWARM_TOKEN 10.0.0.2:2377
```

I deployed the container images, which I had pushed to GHCR, and pulled with `--with-registry-auth` to allow access from the server to GHCR. There were two images, the `api` image and the `worker` image. The API managed a list of search areas (the areas around the points found from overpass turbo), giving search areas to workers, and expanding the search radius by 500 meters when yurts were found. The workers requested search areas from the API and sent back a list of yurts found within the search areas.

#### API

I used FastAPI to build the API, in which there were two routes.

*   GET /search-area - Workers sent a request to this route to get a search area to search.

This route first checks if there are any stale areas, where a worker had requested a search area but never finished it. The workers should send periodic health checks to the API, if this fails then it will return the search area to a different worker after one minute.

```
stale_area = (
    db.query(SearchArea)
    .filter(SearchArea.searching == True)
    .filter(SearchArea.health_check < one_minute_ago)
    .with_for_update()
    .first()
)
```

If there are no stale search areas, then a new point will be selected at random, and the search area will be increased if there have been previous searches.

```
point = (
    db.query(Point)
    .options(joinedload(Point.search_areas))
    .filter(Point.searched == False)
    .filter(~Point.search_areas.any(SearchArea.searched == False))
    .order_by(func.random())
    .first()
)

if not point:
    raise HTTPException(
        status_code=404, detail="No available point to search")

previous_areas = [sa for sa in point.search_areas]
if previous_areas:
    max_meters = max(area.meters for area in previous_areas)
    new_meters = max_meters + 500
else:
    new_meters = 500
```

A `SearchArea` has a list of tiles that are inside it. Each `Tile` has as status of `searched`. I used geopandas, as shown earlier, to generate a bounding box over the search area and create a list of tiles. For each of these tiles, I check the database to see if they have already been created + searched. If they haven’t then they are upserted and assigned to the search area.

```
created_tiles = (
    db.query(Tile)
    .filter(
        tuple_(Tile.x, Tile.y, Tile.z).in_(
            [(tile["x"], tile["y"], tile["z"])
             for tile in tiles_to_create]
        )
    )
    .all()
)

new_area.tiles.extend(created_tiles)
```

The route returns the search area, containing a list of tiles to search.

*   POST /search-area/:id - Workers sent a request containing the yurts to this route.

This route inserts the yurts into the database, and marks the `Point`, `SearchArea`, and `Tile` as searched as needed. The `Point` gets marked as searched if no yurts are found, and the `SearchArea` and `Tile` are marked as searched.

```
if len(yurts_to_create) > 0:
    stmt = insert(Yurt).values(yurts_to_create)
    stmt = stmt.on_conflict_do_nothing(
        index_elements=["longitude", "latitude"])
    db.execute(stmt)
else:
    db.execute(
        update(Point).where(
            exists().where(
                (SearchArea.point_id == Point.id) & (Point.id == id)
            )
        ).values(
            searched=True,
        )
    )
```

#### Worker

The worker script ran in a loop until it encountered the `No available point to search` error. This loop consisted of requesting the `/search-area` to get a list of tiles to search, downloading each tile, then passing the tile image to the model to detect yurts. Finally, the worker sends a list of yurts to the API.

```
def find_yurts(x, y, z):
    filepath = os.path.join("tiles", "{}_{}_{}.jpeg".format(x, y, z))

    results = model(filepath, imgsz=256)

    yurts = []
    for result in results:
        for prediction in result.boxes:
            xyxy = prediction.xyxy[0].tolist()

            # Find center of the bounding box
            pixel_x = xyxy[0] + (xyxy[2] - xyxy[0]) / 2
            pixel_y = xyxy[1] + (xyxy[3] - xyxy[1]) / 2

            lat, lon = tile_xyz_to_lonlat(x, y, z, pixel_x, pixel_y)

            yurts.append({
                "latitude": lat,
                "longitude": lon,
                "score": prediction.conf.item(),
            })

    return yurts
```

I began scaling this service slowly and eventually ramped up to 120 workers running in parallel using `docker service scale worker=120`. Each container processed its assigned tile, and if yurts were found, posted their coordinates to the API.

### The resulting count

After searching a couple million tiles I downloaded the yurt dataset, which I uploaded [here (12mb file)](https://cdn.monroeclinton.com/yurts.json). In total I found 172,689 yurts with a prediction score of greater than 40%.

Perhaps there’s some lonesome yurts far in the Gobi Desert or the Altai Mountains I missed, so we could add a hundred or so for those. I could have also done more like providing image context and training on more data from smaller towns, but I only have so much time.

For fun I did some querying using [PostGIS](https://postgis.net/) to find areas with high concentrations of yurts. Generally I found places that are hotels or remote areas near mines.

![Image 7: Many yurts](https://monroeclinton.com/counting-all-yurts-in-mongolia/many-yurts.jpeg)

> Maps Data: Google © 2025 Airbus, CNES / Airbus, Maxar Technologies

The people of the yurts
-----------------------

Historically, yurts have been a home for the nomadic peoples of the steppe to live. As Mongolia developed into the modern world, the usage of yurts changed with the country. For example, I found a reference to yurts being used as makeshift schools in the early 1900s. This period was the start of the transformation from a nomadic herder society to an urban industrial society.

> In the rural areas, in addition to the existing 60 scribe schools, at least 49 state primary schools were established by 1917. They were largely housed in yurts and financed with state, municipal, and private funds. (Steiner-Khamsi and Stolpe 36)

This reflects the developmental history of Mongolia, and how people are adjusting to the modern world. Mongolia has transitioned from a mostly nomadic herder society, to a mostly urbanized industrial society. As people transition from one system of life to another, remnants of their old system persist. Housing and infrastructure are expensive, so as Mongolia transformed, once nomadic herders took their yurts to urban areas and continued living in them.

> The 51 percent urban population reported in the 1979 census reflected rapid migration to the cities in the 1970s. The influx of rural people created housing problems, among them long waits for assignment to an apartment, expansion of ger districts on the edges of built-up areas, and pressure to invest in more housing, roads, and other urban infrastructure. (Worden et al. 86)

Due to the large number of people moving to urban locations, it has been difficult for the government to build the infrastructure needed for them. The informal settlements that grew from this difficulty are now known as ger districts. There have been many efforts to formalize and develop these areas. The Law on Allocation of Land to Mongolian Citizens for Ownership, passed in 2002, allowed for existing ger district residents to formalize the land they settled, and allowed for others to receive land from the government into the future.

Along with the privatization of land, the Mongolian government has been pushing for the development of ger districts into areas with housing blocks connected to utilities. The plan for this was published in 2014 as Ulaanbaatar 2020 Master Plan and Development Approaches for 2030. Although progress has been slow (Choi and Enkhbat 7), they have been making progress in building housing blocks in ger distrcts. Residents of ger districts sell or exchange their plots to developers who then build housing blocks on them. Often this is in exchange for an apartment in the building, and often the value of the apartment is less than the land they originally had (Choi and Enkhbat 15).

Based on what I’ve read about the ger districts, they have been around since at least the 1970s, and progress on developing them has been slow. When ineffective policy results in a large chunk of the populace generationally living in yurts on the outskirts of urban areas, it’s clear that there is failure. One of the most important functions of government is inspiring the citizenry to achieve greatness. Most governments around the world fail in this, but we should all work towards it. I think a step the Mongolian government could take for this is to analyze which policy failures have led to such slow progress on the ger district issue.

The Mongolian government’s long-term vision is to provide utilities and good housing for these areas. Although I can’t contribute anything to this vision, I wish for the best success in this plan. I’m glad to have learned about a country and people I used to know nothing about. Hopefully in the future I’ll study more about Mongolia, but for now I’m off to my next project.

### Further questions

*   What causes Mongolia and other countries to urbanize and industrialize?
*   Why do some Mongolians head to the cities and others stay?
*   What challenges does the Mongolian government face in developing ger districts?
*   What causes the difference in speed of development between countries?

References
----------

*   Choi, Mack Joong, and Urandulguun Enkhbat. “Distributional Effects of Ger Area Redevelopment in Ulaanbaatar, Mongolia.” International Journal of Urban Sciences, vol. 24, no. 1, Jan. 2020, pp. 50–68. DOI.org (Crossref), [https://doi.org/10.1080/12265934.2019.1571433](https://doi.org/10.1080/12265934.2019.1571433).

*   City of Ulaanbaatar. _Ulaanbaatar 2020 Master Plan and Development Approach for 2030._ 2014.

*   Steiner-Khamsi, Gita, and Ines Stolpe. _Educational Import: Local Encounters with Global Forces in Mongolia._ 1st ed, Palgrave Macmillan, 2006.

*   Worden, Robert L, et al. _Mongolia: A Country Study._ Washington, D.C.: Federal Research Division, Library of Congress: For sale by the Supt. of Docs., U.S. G.P.O, 1991. Pdf. Retrieved from the Library of Congress, <www.loc.gov/item/90006289/>.

*   Yang, Jeasurk, et al. _Poverty Mapping in Mongolia with AI-Based Ger Detection Reveals Urban Slums Persist after the COVID-19 Pandemic._ arXiv:2410.09522, arXiv, 12 Oct. 2024. _arXiv.org_, [https://doi.org/10.48550/arXiv.2410.09522](https://doi.org/10.48550/arXiv.2410.09522).
