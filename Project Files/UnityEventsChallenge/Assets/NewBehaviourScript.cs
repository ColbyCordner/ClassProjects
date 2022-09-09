
using UnityEngine;
using UnityEngine.Events;

public class NewBehaviourScript : MonoBehaviour
{
    public UnityEvent pickupEvent;
    public Material red;
    public Material blue;
    public GameObject GameObject;
        
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void OnTriggerEnter(Collider other)
    {
        pickupEvent.Invoke();
    }

    public void pickUp()
    {
        GameObject.GetComponent<MeshRenderer>().material = blue;
    }
}
