using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ColorMatchBehavior : MatchBehavior
{
    public ColorIDDataList colorIDDataListObj;

//Sets the Color ID of the object as whatever color the object currently is
    private void Awake()
    {
        idObj = colorIDDataListObj.currentColor;

    }

    public void ChangeColor(SpriteRenderer renderer)
    {
        var newColor = idObj as ColorID;
        renderer.color = newColor.value;
    }
}
