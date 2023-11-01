# mock_data

Example using the test client: 
```shell
source ~/venv/bin/activate
python ./event_test_client.py -f /tmp/nb_event_updated_ip.json
...
<Response [200]>
```

Curl example: 
```shell
sig=$(cat /tmp/nb_event_updated_ip.json | openssl dgst -sha512 -hmac "*****" | awk '{print "X-Hub-Signature: "$2}')
curl -X POST -H "Content-Type: application/json" \
-H "${sig}" --data "@/tmp/nb_event_updated_ip.json" \
 http://localhost:8082/v1/webhook/device

```

## nb_event_device_created.json
A newly created device.  
* newly created device has event type `updated`
* snapshots.differences.removed is always None
* snapshots.differences.prechange is always None

## nb_event_device_updated.json
An updated device.
* has event type `updated'
* snapshots.differences.[pre|post]change are populated
* snapshots.differences.removed is populated

## nb_event_device_deleted.json
A deleted device.
has event type `deleted`
* snapshots.differences.added is always None
* snapshots.differences.postchange is always None