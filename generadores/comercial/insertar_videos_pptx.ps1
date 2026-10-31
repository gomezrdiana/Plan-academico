# Reemplaza cada imagen llamada VIDEO::archivo por el video nativo de PowerPoint (se reproduce al entrar a la diapositiva)
param([string]$Pptx)
$dir = Split-Path $Pptx
$pp = New-Object -ComObject PowerPoint.Application
$p = $pp.Presentations.Open($Pptx, $false, $false, $false)
foreach ($sl in $p.Slides) {
  $marcas = @(); foreach ($sh in $sl.Shapes) { if ($sh.Name -like 'VIDEO::*') { $marcas += $sh } }
  $n = 0
  foreach ($sh in $marcas) {
    $file = Join-Path $dir ($sh.Name.Substring(7))
    $l=$sh.Left; $t=$sh.Top; $w=$sh.Width; $h=$sh.Height
    $sh.Delete()
    $v = $sl.Shapes.AddMediaObject2($file, 0, -1, $l, $t, $w, $h)
    $n++
    if ($marcas.Count -eq 1) { $v.AnimationSettings.PlaySettings.PlayOnEntry = -1 }
    "slide $($sl.SlideIndex): $($file | Split-Path -Leaf) ms=$($v.MediaFormat.Length)"
  }
}
$p.Save(); $p.Close(); $pp.Quit()
