const SAMPLE_PRODUCTS = ["FixedBond", "VanillaSwap", "CRS", "Option"];

async function loadPricingSamples() {
  const samples = {};
  await Promise.all(
    SAMPLE_PRODUCTS.map(async function (name) {
      const [tomlRes, jsonRes] = await Promise.all([
        fetch("api/toml/" + name + ".toml"),
        fetch("api/json/" + name + ".json")
      ]);
      if (!tomlRes.ok) throw new Error("샘플 TOML을 불러오지 못했습니다: " + name);
      if (!jsonRes.ok) throw new Error("샘플 JSON을 불러오지 못했습니다: " + name);
      samples[name] = {
        toml: await tomlRes.text(),
        json: JSON.stringify(await jsonRes.json(), null, 2)
      };
    })
  );
  return samples;
}
