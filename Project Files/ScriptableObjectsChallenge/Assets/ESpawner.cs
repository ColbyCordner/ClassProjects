using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ESpawner : MonoBehaviour
{
    [SerializeField] EnemySpawner[] ES;

    [SerializeField] float BetweenWaveDelayMain = 3; 
    float betweenWaveDelay;

    private int currentES = 0;
    private int spawned = 0;
    private float spawnDelayMain = 0;
    private float spawnDelay = 0;
        
    // Start is called before the first frame update
    void Start()
    {
        betweenWaveDelay = BetweenWaveDelayMain;

        spawnDelayMain = ES[currentES].spawnDelay;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
