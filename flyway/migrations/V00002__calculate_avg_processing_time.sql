DO 
$$
DECLARE
	v_job_id	BIGINT;
BEGIN 

   CREATE TABLE IF NOT EXISTS completed_order_time_series(
		id 						BIGSERIAL PRIMARY KEY,
		date					TIMESTAMP WITH ZONE
		total_no_of_orders		BIGINT NOT NULL,
		total_processing_time	BIGINT NOT NULL
   );

   cron.schedule('completed_order_time_series', '1 0 * * *', 'select fn_completed_order_time_series_update()')
   
END
$$