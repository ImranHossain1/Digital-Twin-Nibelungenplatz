# Upload and configure POI on Dassault platform

1. Upload the camera.geojson file to DS via `City Upload Assistant` --> click Add file --> Select your collaborative space --> click Create

    ![](/configure_dassault_static_data/img/img_cameras/cameracityupload.png)

2. Open `City Referential` --> click `+` icon to add dataset to your referential --> select Points of Interest --> drag and drop the dataset from your `3DSpace` --> provide the description --> click Next --> click Next --> click Ok

    ![](/configure_dassault_static_data/img/img_cameras/createdataset.png)

    ![](/configure_dassault_static_data/img/img_cameras/camerasdataset.png)

    ![](/configure_dassault_static_data/img/img_cameras/transferringcameras.png)

    ![](/configure_dassault_static_data/img/img_cameras/cameras_transferred.png)

3. Select the dataset which has been uploaded in Step 2 and click on Configure (gear icon - first icon on the right corner)

    ![](/configure_dassault_static_data/img/img_cameras/configurecameras.png)

4. Click Next --> click Next --> click Ok. And wait until the state of the dataset reaches to "Ready".

    ![](/configure_dassault_static_data/img/img_cameras/cameranext1.png)

    ![](/configure_dassault_static_data/img/img_cameras/cameranext2.png)

    ![](/configure_dassault_static_data/img/img_cameras/cameranext3.png)

    ![](/configure_dassault_static_data/img/img_cameras/preparing_cameras.png)

    ![](/configure_dassault_static_data/img/img_cameras/ready_buildings.png)

5. Now, drag and drop TrafficCamera.3dxml file from your `3DSpace` on to the `City Discover` on the point of interests

    ![](/configure_dassault_static_data/img/img_cameras/camerasicon.png)

6. Resizing the camera icon - Select the item --> Go to Settings --> under Properties --> representation --> Shape --> Scale - 0.01 or 0.015

7. Under Properties --> under General --> under Name --> Change the name to Camera1, Camera2, Camera3 and Camera4 for each temporary items respectively

    ![](/configure_dassault_static_data/img/img_cameras/cameras_names.png)

8. Under General --> under transformation --> under translation --> Adjust the Rotation - Camera1(building 9) - 159 degree, Camera2 - 230 degree, Camera3 - 346 degree, Camera4 - 46 degree

    ![](/configure_dassault_static_data/img/img_cameras/cameras_rotation.png)

9. Under Fill --> select any color of your choice (#453c3c/#3d72d4)

    ![](/configure_dassault_static_data/img/img_cameras/cameras_scale_fill.png)

10. Save the Experience. The above created Camera items are temporary. They have to be moved and placed under the Buildings, Trees and Basemap datasets to save permanently. Once all the changes are finished, move the Camera items to the Experience where rest of the static data is present (drag the Camera items from Temporary branch and place them under the saved Experience). Now, Cameras will look like one of the branches in the newly saved Experience as similar to other data. Now again, save the Experience.

    ![](/configure_dassault_static_data/img/img_cameras/cameras_temporaryitems.png)

11. Here is the final view of the `City Discover` consisting of all the static data :)

    ![](/configure_dassault_static_data/img/img_cameras/final_city_discover.png)
