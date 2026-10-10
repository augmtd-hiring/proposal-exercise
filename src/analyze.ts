// Entry point: npm run analyze -- <data-dir> <out-dir>
// Writes out/proposal.md, out/sources.json and out/model_log.jsonl (see README.md).

const [dataDir, outDir] = process.argv.slice(2);

if (!dataDir || !outDir) {
  console.error('usage: npm run analyze -- <data-dir> <out-dir>');
  process.exit(2);
}

console.error(`not implemented yet (data: ${dataDir}, out: ${outDir})`);
process.exit(1);
