using UnityEngine;
using System.Collections;

public class camera_movement : MonoBehaviour {

	public GameObject player;

	private Vector3 offset;

	// Use this for initialization
	void Start () {
		offset = transform.position - player.transform.position;
	}
	
	// Update is called once per frame
	// LateUpdate is called once all items in Update have been processed
	// This means that we know for sure that the player has moved for that frame before we try to re-position the camera.
	void LateUpdate () {
		transform.position = player.transform.position + offset;
	}
}
