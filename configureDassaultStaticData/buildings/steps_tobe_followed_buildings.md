# Upload and configure Buildings on Dassault platform

1. Run the python script on building.geojson and generate a new dataset with adjusted building height

2. Upload the dataset to DS via `City Upload Assistant` --> click Add file --> Select your Collaborative space --> click Create

    ![](/configure_dassault_static_data/img/img_buildings/datasetviacityupload.png)

3. Open `City Referential` --> click `+` icon to add dataset to your referential --> select Buildings as the category --> drag and drop the cleaned new building dataset --> provide the Description --> click Next --> click Next --> click Ok

    ![](/configure_dassault_static_data/img/img_buildings/building_create.png)

    ![](/configure_dassault_static_data/img/img_buildings/transferring.png)

    ![](/configure_dassault_static_data/img/img_buildings/transferred.png)

4. Select the dataset which has been uploaded in Step 3 and click on Configure (gear icon - first icon on the right corner)

5. Under Map tab --> select the building height column for Height parameter --> click Next --> click Next --> click Ok

    ![](/configure_dassault_static_data/img/img_buildings/configure_building_height.png)

    ![](/configure_dassault_static_data/img/img_buildings/next2.png)

    ![](/configure_dassault_static_data/img/img_buildings/next3.png)

    ![](/configure_dassault_static_data/img/img_buildings/next4.png)

6. And wait until the state of the dataset reaches to "Ready".

    ![](/configure_dassault_static_data/img/img_buildings/preparing.png)

    ![](/configure_dassault_static_data/img/img_buildings/ready_buildings.png)

7. Now, refresh the `City Discover` and you should be able to see the newly uploaded dataset

8. Right click on it and add it to the Experience or drag and drop the dataset to the Map.
