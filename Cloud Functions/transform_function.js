function jsonConvertor(t) {
  try {
    let z = JSON.stringify(JSON.parse(t));
    return JSON.parse(z);
  } catch (e) {
    console.log(`The following has been failed with the following ${e}`);
  }
}

